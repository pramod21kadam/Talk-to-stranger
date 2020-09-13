from init import socketio as socket
from packages.packages import *

@socket.on("connect")
def conntect():
    print (f"{(request.sid)} connected the room with ip {request.remote_addr}")
    if len(clients) == 0:
        clients.append(request.sid)
    else:
        emit('partner',{ "user": request.sid }, room= clients[-1] )
        emit('partner',{ "user": clients[-1] }, room= request.sid )
        clients.pop()

@socket.on("disconnect")
def disconnect():
    if request.sid in clients:
        clients.remove(request.sid)
    print(f"{request.sid} disconnected")

@socket.on('message')
def handleMessage(data):
    print(data)
    emit('message', data, room = data['to'])