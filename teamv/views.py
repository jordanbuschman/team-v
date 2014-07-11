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

import os

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
    mytemplate = mylookup.get_template('index.mak')
    result = mytemplate.render(title = 'Team Valente - Meeting #{0}'.format(this_meeting), meeting = this_meeting)
    return Response(result)

@view_config(route_name='transcript', renderer='mako')
def transcript(request):
    if 'meeting' in request.GET and is_number(request.GET.get('meeting')):
        file_name = 'teamv/templates/logs/log_{0}.mak'.format(request.GET.get('meeting'))
        if os.path.isfile(file_name):
            mytemplate = mylookup.get_template('transcript.mak')
            this_meeting = request.GET.get('meeting')
            result = mytemplate.render(title = 'Team Valente - Transcript #{0}'.format(this_meeting), meeting = this_meeting)
            return Response(result)
        else:
            return not_found(request)
    else:
        return not_found(request)

@view_config(route_name='start_meeting')
def start_meeting(request):
    if 'meeting' in request.GET and is_number(request.GET.get('meeting')):
        file_name = 'teamv/templates/logs/log_{0}.mak'.format(request.GET.get('meeting'))
        if os.path.isfile(file_name): # If the meeting has already been created
            return Response(status = '400 Bad Request')
        else:
            open(file_name, 'w').close()
            return Response(status = '201 Created')
    else:
        return Response(status = '400 Bad Request')
            
@view_config(route_name='socketio')
def socketio(request):
    socketio_manage(request.environ, { '/chat': ChatNamespace }, request=request)
    return Response('')
