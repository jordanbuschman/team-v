from pyramid.httpexceptions import HTTPNotFound
from pyramid.response import Response
from pyramid.response import FileResponse
from pyramid.request import Request
from pyramid.view import view_config
from socketio.namespace import BaseNamespace
from socketio import socketio_manage
from mako.template import Template
from mako.lookup import TemplateLookup
from chat import ChatNamespace
from os import environ, path
from dbconnect import connect_to_db
from hashlib import sha1
from email.utils import formatdate

import os, time, datetime, logging, requests
import boto
import boto.s3.connection
import hmac, binascii

mylookup = TemplateLookup(directories=['teamv/templates'], module_directory='teamv/temp/mako_modules', collection_size=500)

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

@view_config(context=HTTPNotFound, renderer='mako')
def not_found(request):
    mytemplate = mylookup.get_template('not_found.mak')
    result = mytemplate.render(title = 'Team Valente - Page not found')
    return Response(result, status = '404 Not Found')

@view_config(route_name='home', renderer='mako')
def index(request):
    if 'meeting' in request.GET and 'nickname' in request.GET:
        mytemplate = mylookup.get_template('index.mak')
        this_meeting = request.GET.get('meeting')
        this_nickname = request.GET.get('nickname')
        file_name = 'teamv/templates/logs/log_{0}.log'.format(this_meeting)

        data = {'meeting': request.GET.get('meeting')}
        response = requests.post('http://team-v.herokuapp.com/start', data=data)

        if response.status_code == 200 or response.status_code == 201:
            result = mytemplate.render(title = 'Team Valente - Meeting {0}'.format(this_meeting), meeting = this_meeting, nickname = this_nickname)
        elif response.status_code == 403:
            # TODO: Redirect to a page telling you that the meeting is over, but you can see the transcript on the CDN
            print 'This is SUPPOSED to redirect to a page telling you that you can view the now-over meeting\'s transcript, but for now, not found.'
            return not_found(request)
        else: # Bad request, return not found
            return not_found(request)
    else:
        mytemplate = mylookup.get_template('index.mak')
        result = mytemplate.render(title = 'Team Valente - Enter meeting', meeting = None, nickname = None)
    return Response(result)
    
@view_config(route_name='authorization', renderer='json')
def authorization(request):
    if 'meeting' in request.POST and is_number(request.POST.get('meeting')):
        file_name = 'log_{0}.log'.format(request.POST.get('meeting'))
        timestamp = formatdate(localtime=True)
        
        string_to_sign = 'GET\n\n\n{0}\n/teamvlogfiles/{1}'.format(timestamp, file_name)
        hashed_string_to_sign = hmac.new(os.environ['AWS_SECRET_ACCESS_KEY'], string_to_sign, sha1)
        signature = binascii.b2a_base64(hashed_string_to_sign.digest()).rstrip('\n')
        auth = 'AWS' + ' ' + os.environ['AWS_ACCESS_KEY_ID'] + ':' + signature
        # Check out http://docs.aws.amazon.com/AmazonS3/latest/dev/RESTAuthentication.html#UsingTemporarySecurityCredentials for how to give authorization
        return {'text': '200 OK', 'status': 200, 'auth': auth}
    else:
        request.response.status = 400
        return {'text': '400 Bad Request', 'status': 400}

@view_config(route_name='transcript', renderer='mako')
def transcript(request):
    this_meeting = request.matchdict.get('meeting')

    if is_number(this_meeting):
        conn = connect_to_db()
        cur = conn.cursor()

        cur.execute('SELECT time_started, time_finished FROM meetings WHERE meeting=%s', (this_meeting, ))
        result = cur.fetchone()

        cur.close()
        conn.close()

        file_name = 'teamv/templates/logs/log_{0}.log'.format(this_meeting)
        if result is None:
            return not_found(request)
        elif result[0] is not None and result[1] is None and os.path.isfile(file_name): # Meeting is in process and still in local memory
            mytemplate = mylookup.get_template('transcript.mak')
            result = mytemplate.render(title = 'Team Valente - Transcript {0}'.format(this_meeting), meeting = this_meeting, is_local = True)
            return Response(result)
        elif result[0] is not None and result[1] is not None: # Meeting is done, must be in CDN
            # TODO: If log is in CDN, retrieve it
            print 'Must get file from CDN.'
            mytemplate = mylookup.get_template('transcript.mak')
            result = mytemplate.render(title = 'Team Valente - Transcript {0}'.format(this_meeting), meeting = this_meeting, is_local = False)
            return Response(result)
        else: # Something went wrong
            return not_found(request)
    else:
        return not_found(request)

@view_config(route_name='start_meeting', request_method='POST')
def start_meeting(request):
    if 'meeting' in request.POST and is_number(request.POST.get('meeting')):
        file_name = 'teamv/templates/logs/log_{0}.log'.format(request.POST.get('meeting'))
        conn = connect_to_db()
        cur = conn.cursor()

        cur.execute('SELECT time_started, time_finished FROM meetings WHERE meeting=%s', (request.POST.get('meeting'), ))
        result = cur.fetchone()

        if result is None and not os.path.isfile(file_name): # Meeting is open but not created, so create it
            open(file_name, 'w').close()
            cur.execute('INSERT INTO meetings (meeting) VALUES (%s)', (request.POST.get('meeting'), ))
            print 'INSERT INTO meetings (meeting) VALUES ({0})'.format(request.POST.get('meeting'))
            cur.close()
            conn.close()
            return Response(status = '201 Created')
        elif result[0] is not None and result[1] is None and os.path.isfile(file_name): # Meeting is still going, it is OK to join
            cur.close()
            conn.close()
            return Response(status = '200 OK')
        elif result[0] is not None and result[1] is not None: # Meeting has ended, forbidden
            cur.close()
            conn.close()
            return Response(status = '403 Forbidden')
        else: # Something has gone wrong, meeting not found
            cur.close()
            conn.close()
            logging.error('Meeting could not be created or joined')
            return Response(status = '404 Not Found')
    else: # Invalid request
        return Response(status = '400 Bad Request') # No meeting number specified, bad request

@view_config(route_name='end_meeting', request_method='POST')
def end_meeting(request):
    if 'meeting' in request.POST and is_number(request.POST.get('meeting')):
        conn = connect_to_db()
        cur = conn.cursor()

        cur.execute('SELECT id, time_finished FROM meetings WHERE meeting=%s', (request.POST.get('meeting'), ))
        result = cur.fetchone()

        if result is None or result[0] is None or result[1] is not None: # Meeting you want to end does not exist
            cur.close()
            conn.close()
            return Response(status = '400 Bad Request')
        else: # Meeting is found, end meeting and move transcript to CDN
            cur.execute('UPDATE meetings SET time_finished = NOW() WHERE id = %s', (result[0], ))
            print 'UPDATE meetings SET time_finished = NOW() WHERE id = {0}'.format(result[0])

            file_name = 'log_{0}.log'.format(request.POST.get('meeting'))
            file_path = 'teamv/templates/logs/{0}'.format(file_name)
            _file = open(file_path, 'r')
            file_data = _file.read()
            _file.close()

            # Upload the completed file to Amazon S3
            access_key = os.environ['AWS_ACCESS_KEY_ID']
            secret_key = os.environ['AWS_SECRET_ACCESS_KEY']

            connection = boto.s3.connect_to_region('us-west-1',
                aws_access_key_id = access_key,
                aws_secret_access_key = secret_key,
                is_secure=False,
                calling_format = boto.s3.connection.OrdinaryCallingFormat(),
                )

            bucket = connection.get_bucket('teamvlogfiles', validate=False)

            key = bucket.new_key(file_name)
            key.set_contents_from_string(file_data)

            os.remove(file_path) # Delete old file

            cur.close()
            conn.close()
            return Response(status = '200 OK')
    else:
        return Response(status = '400 Bad Request')
            
@view_config(route_name='socketio')
def socketio(request):
    socketio_manage(request.environ, { '/chat': ChatNamespace }, request=request)
    return Response('')
