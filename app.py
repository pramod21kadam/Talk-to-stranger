import sys
sys.path.insert(0,'./src')
from init import Application

app = Application()
socketio = app.socketio
application = app.application

if __name__ == '__main__':
    socketio.run(debug=False)