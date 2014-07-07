from pyramid.view import view_config
from pyramid.response import Response
from os import environ
from socketio import socketio_manage
from socketio.namespace import BaseNamespace
from chat import ChatNamespace

@view_config(route_name='home', renderer='templates/index.mak')
def my_view(request):
    return {'project': 'team-v'}

@view_config(route_name='socketio')
def socketio(request):
    socketio_manage(request.environ, { '/chat': ChatNamespace }, request=request)
    return Response('')
