import os, socket, select

from paste.deploy import loadapp
from socketio.server import SocketIOServer

if __name__ == "__main__":
    open('transcript.txt', 'w').close() # Make sure transcript is created and empty
    app = loadapp('config:production.ini', relative_to='.')
    SocketIOServer(('0.0.0.0', 5000), app, resource="socket.io").serve_forever()
