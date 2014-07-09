from socketio.server import SocketIOServer
from paste.deploy import loadapp

import os

if __name__ == "__main__":
    open('teamv/templates/logs/log_001.mak', 'w').close() # TODO: This is only a test transcript, we need to create meetings and have a transcript for each meeting 

    port = int(os.environ.get("PORT", 5000))

    app = loadapp('config:production.ini', relative_to='.')
    SocketIOServer(('0.0.0.0', port), app, 
        resource="socket.io", policy_server=True,
        policy_listener=('0.0.0.0', 10843)).serve_forever()
