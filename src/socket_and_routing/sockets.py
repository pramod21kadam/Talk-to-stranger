from flask import request
from .base import *
from flask_socketio import Namespace, emit
import utilities.globals as Global

class SocketNameSpace(Namespace):
    
    def on_connect(self):
        Global.online += 1
        emit("online", Global.online, broadcast = True)

    def on_disconnect(self):
        Global.online -= 1
        if len(Global.clients) == 0:
            roomie, boolean = searchPartner({"sid":request.sid, "ip":request.remote_addr}, Global.rooms)
            if(boolean):
                Global.rooms.remove(roomie)
                roomie.remove({"sid":request.sid, "ip":request.remote_addr})
                emit('leave_room', room = roomie[0]["sid"])
        else:
            Global.clients = []
        try:
            Global.banned_ip.remove(request.remote_addr)
        except:
            pass
        Global.active.remove(request.remote_addr)
        emit("online", Global.online, broadcast = True)

    def on_partner(self):
        try:
            if request.remote_addr in Global.banned_ip:
                emit('reload', room = request.sid)
            else:
                if len(Global.clients) != 0 and Global.clients[0]['sid'] != request.sid:
                    Global.rooms.append([{"sid":request.sid, "ip": request.remote_addr}, Global.clients[0]])
                    emit("partner", {"sid":request.sid, "ip": request.remote_addr}, room = Global.clients[0]['sid'])
                    emit("partner", Global.clients[0], room = request.sid)
                    Global.clients.pop(0)
                else:
                    req = {'sid': request.sid, 'ip': request.remote_addr}
                    Global.clients.append(req)
        except Exception as e:
            print(f"Error in partner: {e}")

    def on_stop_search(self):
        try:
            if request.sid in Global.clients:
                Global.clients.remove(request.sid)
        except Exception as e:
            print(f"Error in stop search: {e}")
    
    def on_message(self, data):
        data["from"] = request.sid
        emit('message', data, room = data['to'])
    
    def on_leave_room(self, data):
        if data['partner'] != None:
            emit('leave_room', room=data['partner'])
    
    def on_typing(self, data):
        emit('typing',room = data['partner'])
