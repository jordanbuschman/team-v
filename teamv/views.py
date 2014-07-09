from pyramid.view import view_config
from pyramid.response import Response
from pyramid.response import FileResponse
from os import environ, path
from socketio import socketio_manage
from socketio.namespace import BaseNamespace
from chat import ChatNamespace
from mako.lookup import TemplateLookup
from mako.template import Template

mylookup = TemplateLookup(directories=['./teamv/templates'])

@view_config(route_name='home', renderer='mako')
def index(request):
    mytemplate = mylookup.get_template('index.mak')
    result = mytemplate.render()
    return Response(result)

@view_config(route_name='transcript', renderer='mako', request_method='GET')
def transcript(request):
    if 'meeting_id' in request.GET:
        file_name = 'transcript_{0}.log'.format(request.GET.get('meeting_id'))
        if os.path.isfile(file_name):
            mytemplate = mylookup.get_template('transcript.mak')
            result = mytemplate.render(transcript = file_name)
            return Response(result)
        else:
            mytemplate = mylookup.get_template('not_found.mak')
            request.response.status = '404 Not Found'
            result = mytemplate.render()
            return Response
    else:
        mytemplate = mylookup.get_template('not_found.mak')
        request.response.status = '404 Not Found'
        result = mytemplate.render()
        return Response

@view_config(route_name='socketio')
def socketio(request):
    socketio_manage(request.environ, { '/chat': ChatNamespace }, request=request)
    return Response('')
