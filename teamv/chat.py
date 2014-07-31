from socketio.namespace import BaseNamespace
from socketio.mixins import RoomsMixin, BroadcastMixin
from datetime import datetime

import os, time

class ChatNamespace(BaseNamespace, RoomsMixin, BroadcastMixin):
    nicknames = []
    start_time = None

    def on_chat(self, msg):
        current_time = time.strftime("%H:%M:%S")
        time_elapsed = datetime.strptime(current_time, '%H:%M:%S') - datetime.strptime(self.start_time, '%H:%M:%S')

        self.emit_to_room(self.room, 'chat', '{0}: {1}'.format(self.socket.session['nickname'], msg.lstrip()))
        with open('teamv/templates/logs/log_{0}.log'.format(self.room), 'a') as f:
            f.write('({0}) {1}: {2}\n'.format(time_elapsed, self.socket.session['nickname'], msg.lstrip()))
    
    def on_join(self, room):
        self.room = room
        self.join(room)

    def on_nickname(self, nickname):
        current_time = time.strftime("%H:%M:%S")
        self.nicknames.append(nickname)
        if self.start_time is None:
            self.start_time = time.strftime("%H:%M:%S")

        time_elapsed = datetime.strptime(current_time, '%H:%M:%S') - datetime.strptime(self.start_time, '%H:%M:%S')

        self.socket.session['nickname'] = nickname
        self.emit_to_room(self.room, 'user_connect', nickname)
        with open('teamv/templates/logs/log_{0}.log'.format(self.room), 'a') as f:
            f.write('({0}) {1} connected\n'.format(time_elapsed, nickname))

    def on_end(self):
        self.emit_to_room(self.room, 'end')

    def recv_disconnect(self):
        current_time = time.strftime("%H:%M:%S")
        time_elapsed = datetime.strptime(current_time, '%H:%M:%S') - datetime.strptime(self.start_time, '%H:%M:%S')

        nickname = self.socket.session['nickname']
        self.emit_to_room(self.room, 'user_disconnect', nickname)
        self.nicknames.remove(nickname)
        with open('teamv/templates/logs/log_{0}.log'.format(self.room), 'a') as f:
            f.write('({0}) {1} disconnected\n'.format(time_elapsed, nickname))
        self.disconnect(silent=True)





