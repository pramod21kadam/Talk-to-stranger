
from flask import Flask
from flask_socketio import SocketIO
import utilities.globals as Global
from socket_and_routing.sockets import SocketNameSpace
from blueprints.api import api

class Application:
    def __init__(self) -> None:
        self.application = Flask(__name__, static_folder="../static", template_folder="../templates")
        
        self.application.config.from_pyfile('../config/config.cfg')
        self.application.register_blueprint(api, url_prefix='/')
        
        self.socketio = SocketIO()
        self.socketio.on_namespace(SocketNameSpace('/'))
        
        self.socketio.init_app(self.application)
    
    # def run(self):
    #     print("Running app ")
    #     self.socketio.run(app=self.application, debug=False)