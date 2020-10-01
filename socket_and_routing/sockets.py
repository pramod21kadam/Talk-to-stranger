from packages.flaskPackages import *
from service._init_ import *
from .base import *
import utilities.globals as Global
import init


socketio = init.socketio

@socketio.on("connect")
def conntect():
    SocketServ().connect(request.remote_addr)
    Global.online += 1
    emit("online", Global.online, broadcast = True)

@socketio.on("disconnect")
def disconnect():
    Global.online -= 1
    print("disconnect")
    SocketServ().disconnect(request.remote_addr)
    if len(Global.clients) == 0:
        roomie, boolean = searchPartner({"sid":request.sid, "ip":request.remote_addr}, Global.rooms)
        if(boolean):
            Global.rooms.remove(roomie)
            roomie.remove({"sid":request.sid, "ip":request.remote_addr})
            emit('leave_room', room = roomie[0]["sid"])
    else:
        Global.clients = []
    emit("online", Global.online, broadcast = True)

@socketio.on("partner")
def search():
    try:
        if len(Global.clients) != 0 and Global.clients[0] != request.sid:
            emit("partner", {"sid":request.sid, "ip": request.remote_addr}, room = Global.clients[0]["sid"])
            emit("partner", Global.clients[0], room = request.sid)
            Global.rooms.append([{"sid":request.sid, "ip": request.remote_addr}, Global.clients[0]])
            Global.clients.pop()
        else:
            req = {"sid": request.sid, "ip": request.remote_addr}
            Global.clients.append(req)
    except Exception as e:
        print(f"Error in partner: {e}")

@socketio.on('stop_search')
def stop_search():
    try:
        if request.sid in Global.clients:
            Global.clients.remove(request.sid)
    except Exception as e:
        print(f"Error in stop search: {e}")


@socketio.on('message')
def handleMessage(data):
    emit('message', data, room = data['to'])

@socketio.on('leave_room')
def leave_room(data):
    if data['partner'] != None:
        emit('leave_room', room=data['partner'])
    
@socketio.on('typing')
def typing(data):
    emit('typing',room = data['partner'])