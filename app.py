from packages.packages import *
# app = Flask(__name__)
# app.config.from_pyfile('config.cfg')
# print(app.secret_key)
# socket = SocketIO()
# app = create_app()

# clients = []
# online = [0]

# @app.route('/', methods = ['GET'])
# def index():
#     return render_template('dashboard.html')

# @socket.on('online')
# def online(data):
#     emit('status_change', {'username': data['username'], 'status': 'online'}, broadcast=True)

# @socket.on('offline')
# def online(data):
#     emit('status_change', {'username': data['username'], 'status': 'offline'}, broadcast = True )

# @socket.on("connect")
# def conntect():
#     online[0] += 1
#     emit('online', online[0], broadcast=True)
#     print (f"{(request.sid)} connected the room with ip {request.remote_addr}")
#     if len(clients) == 0:
#         clients.append(request.sid)
#     else:
#         emit('partner',{ "user": request.sid }, room= clients[-1] )
#         emit('partner',{ "user": clients[-1] }, room= request.sid )
#         clients.pop()

# @socket.on("disconnect")
# def disconnect():
#     online[0] -= 1
#     emit('online', online[0], broadcast=True)
#     if request.sid in clients:
#         clients.remove(request.sid)
#     print(f"{request.sid} disconnected")

# @socket.on('message')
# def handleMessage(data):
#     print(data)
#     emit('message', data, room = data['to'])

if __name__ == '__main__':
    # socket.run(app)
    # app.debug = True
    # app.debug = True
    # app.run(host='192.168.43.209', port="5000")
    app.run(debug=True)