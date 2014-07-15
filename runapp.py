from socketio.server import SocketIOServer
from paste.deploy import loadapp

import os, psycopg2, urlparse

urlparse.uses_netloc.append("postgres")
url = urlparse.urlparse(os.environ["postgres://ucafecrfiuurbq:hM1Oj9Mu6HzYqQrZh8i_vbUc3Q@ec2-107-21-100-118.compute-1.amazonaws.com:5432/d9p38p4gu9mrk0"])

conn = psycopg2.connect(
    database=url.path[1:],
    user=url.username,
    password=url.password,
    host=url.hostname,
    port=url.port
)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))

    app = loadapp('config:production.ini', relative_to='.')
    SocketIOServer(('0.0.0.0', port), app, 
        resource="socket.io", policy_server=True,
        policy_listener=('0.0.0.0', 10843)).serve_forever()
