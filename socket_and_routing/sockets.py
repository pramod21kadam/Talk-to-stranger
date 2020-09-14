from packages.packages import *
from utilities.globals import *
from service._init_ import *

@socket.on("connect")
def conntect():
    online[0] += 1
    emit("online", online[0], broadcast = True)
    try:
        print (f"{(request.sid)} connected the room with ip {request.remote_addr}")
    except Exception as e:
        print(e)
    
    
@socket.on("disconnect")
def disconnect():
    online[0] -= 1
    emit("online", online[0], broadcast = True)
    print(f"{request.sid} disconnected with ip {request.remote_addr}")

@socket.on("partner")
def search():
    try:
        print(f"partner search for {request.sid}")
        if len(clients) != 0:
            print("Created room")
            print(session.get('room'))
            emit("partner", clients[0], room=request.sid)
            emit("partner", request.sid, room=clients[0])
            clients.pop()
        else:
            clients.append(request.sid)
    except Exception as e:
        print(e)

@socket.on('message')
def handleMessage(data):
    emit('message', data, room = data['to'])