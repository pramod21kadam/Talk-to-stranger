import sys
sys.path.insert(0, './src')
from flask import Flask
from flask_socketio import SocketIO
from src.utilities import globals as Global
from src.socket_and_routing.sockets import SocketNameSpace
from src.blueprints.api import api

class Application:
    def __init__(self) -> None:
        self.application = Flask(__name__, static_folder="./static", template_folder="./templates")
        
        self.application.config.from_pyfile('./config/config.cfg')
        self.application.register_blueprint(api, url_prefix='/')
        
        self.socketio = SocketIO()
        self.socketio.on_namespace(SocketNameSpace('/sockets'))
        
        self.socketio.init_app(self.application)
    
    def get_app(self):
        return self.socketio

    def run(self):
        print("Running app ")
        self.socketio.run(app=self.application, debug=False)


instance = Application()
application = instance.application
socketio = instance.socketio
# if __name__ == '__main__':

#     socketio.run(app=application)