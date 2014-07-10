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

mylookup = TemplateLookup(directories=['./teamv/templates'])

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
    result = mytemplate.render()
    return Response(result)

@view_config(route_name='transcript', renderer='mako', request_method='GET')
def transcript(request):
    if 'meeting_number' in request.GET:
        file_name = 'teamv/templates/logs/log_{0}.mak'.format(request.GET.get('meeting_number'))
        if os.path.isfile(file_name):
            mytemplate = mylookup.get_template('transcript.mak')
            this_meeting_number = request.GET.get('meeting_number')
            result = mytemplate.render(title = 'Team Valente - Transcript #{0}'.format(this_meeting_number), meeting_number = this_meeting_number)
            return Response(result)
        else:
            return not_found(request)
    else:
        return not_found(request)

@view_config(route_name='start_meeting', request_method='GET')
def start_meeting(request):
    if 'meeting_number' in request.GET and is_number(request.GET.get('meeting_number')):
        file_name = 'teamv/templates/logs/log_{0}.mak'.format(request.GET.get('meeting_number'))
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
