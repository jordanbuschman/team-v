import os, socket, select

from pyramid.paster import get_app
from socketio.server import SocketIOServer

if __name__ == "__main__":
    open('transcript.log', 'w').close() # Make sure transcript is created and empty

    app = get_app('production.ini')
    SocketIOServer(('0.0.0.0', 5000), app, 
        resource="socket.io", policy_server=True,
        policy_listener=('0.0.0.0', 10843)).serve_forever()
