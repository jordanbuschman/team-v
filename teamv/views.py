from pyramid.view import view_config
from pyramid.response import Response
from pyramid.response import FileResponse
from os import environ
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

@view_config(route_name='transcript')
def transcript(request):
    response = FileResponse(
        'transcript.log',
        request = request,
        content_type='text/plain'
    )
    return response

@view_config(route_name='socketio')
def socketio(request):
    socketio_manage(request.environ, { '/chat': ChatNamespace }, request=request)
    return Response('')
