# from packages.packages import socketio, application
from init import application, socketio
if __name__ == '__main__':
    socketio.run(application, host="127.0.0.1", port=8000)