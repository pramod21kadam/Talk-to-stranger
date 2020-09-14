from init import socketio as socket
from packages.packages import *
from utilities.globals import *
from service._init_ import *
from socket_and_routing.routing import app

@socket.on("connect")
def conntect():
    try:
        SocketServ().post()
        print(SocketServ().getall())
    except Exception as e:
        print(e)
    print (f"{(request.sid)} connected the room with ip {request.remote_addr}")
    
@socket.on("disconnect")
def disconnect():
    print(f"{request.sid} disconnected with ip {request.remote_addr}")

@socket.on("partner")
def search():
    pass

@socket.on('message')
def handleMessage(data):
    print(data)
    emit('message', data, room = data['to'])