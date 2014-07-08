from socketio.server import SocketIOServer
from paste.deploy import loadapp

if __name__ == "__main__":
    open('transcript.log', 'w').close() # Make sure transcript is created and empty

    app = loadapp('config:production.ini', relative_to='.')
    SocketIOServer(('0.0.0.0', 5000), app, 
        resource="socket.io", policy_server=True,
        policy_listener=('0.0.0.0', 10843)).serve_forever()
