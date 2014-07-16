from pyramid.httpexceptions import HTTPNotFound
from pyramid.response import Response
from pyramid.response import FileResponse
from pyramid.view import view_config
from socketio.namespace import BaseNamespace
from socketio import socketio_manage
from mako.template import Template
from mako.lookup import TemplateLookup
from chat import ChatNamespace
from os import environ, path
from dbconnect import connect_to_db

import os, time, datetime

mylookup = TemplateLookup(directories=['./teamv/templates'], module_directory='./teamv/temp/mako_modules', collection_size=500)

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
    # TODO: Redirect if nickname is not specified
    if 'meeting' in request.GET and 'nickname' in request.GET:
        mytemplate = mylookup.get_template('index.mak')
        this_meeting = request.GET.get('meeting')
        this_nickname = request.GET.get('nickname')
        file_name = 'teamv/templates/logs/log_{0}.mak'.format(this_meeting)
        response = start_meeting(request)
        print response.time_created

        if response.status == '201 Created' or response.status == '200 OK':
            result = mytemplate.render(title = 'Team Valente - Meeting {0}'.format(this_meeting), meeting = this_meeting, nickname = this_nickname)
        else: # Bad request, return not found
            return not_found(request)
    else:
        mytemplate = mylookup.get_template('index.mak')
        result = mytemplate.render(title = 'Team Valente - Enter meeting', meeting = None, nickname = None)
    return Response(result)
    
@view_config(route_name='transcript', renderer='mako')
def transcript(request):
    if 'meeting' in request.GET and is_number(request.GET.get('meeting')):
        file_name = 'teamv/templates/logs/log_{0}.mak'.format(request.GET.get('meeting'))
        if os.path.isfile(file_name):
            mytemplate = mylookup.get_template('transcript.mak')
            this_meeting = request.GET.get('meeting')
            result = mytemplate.render(title = 'Team Valente - Transcript {0}'.format(this_meeting), meeting = this_meeting)
            return Response(result)
        else:
            return not_found(request)
    else:
        return not_found(request)

@view_config(route_name='start_meeting')
def start_meeting(request):
    if 'meeting' in request.GET and is_number(request.GET.get('meeting')):
        file_name = 'teamv/templates/logs/log_{0}.mak'.format(request.GET.get('meeting'))
        conn = connect_to_db()
        cur = conn.cursor()

        if os.path.isfile(file_name): # If the meeting has already been created, check if the meeting has ended
            cur.execute('SELECT time_started, time_finished FROM meetings WHERE meeting=%s', (request.GET.get('meeting'), ))
            result = cur.fetchone()
            cur.close()
            conn.close()
        
            if result is None:
                return Response(status = '404 Not Found') # Something has gone wrong, meeting not found
            elif result[1] is not None:
                return Response(status = '403 Forbidden') # Meeting has ended, forbidden
            else:
                return Response(status = '200 OK') # Meeting is still going, it is OK to join
        else:
            open(file_name, 'w').close()
            cur.execute('INSERT INTO meetings (meeting) VALUES (%d)', (request.GET.get('meeting'), ))
            cur.close()
            conn.close()
            return Response(status = '201 Created') # Meeting has not been started yet, so it is created
    else: # Invalid request
        return Response(status = '400 Bad Request') # No meeting number specified, bad request
            
@view_config(route_name='socketio')
def socketio(request):
    socketio_manage(request.environ, { '/chat': ChatNamespace }, request=request)
    return Response('')
