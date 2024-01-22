from packages.flaskPackages import *
import utilities.globals as Global
from socket_and_routing.sockets import SocketNameSpace
from blueprints.api import api

class Application:
    def __init__(self) -> None:
        self.application = Flask(__name__)
        
        self.application.config.from_pyfile('config.cfg')
        self.application.register_blueprint(api, url_prefix='/')
        
        self.socketio = SocketIO()
        self.socketio.on_namespace(SocketNameSpace('/'))
        
        self.socketio.init_app(self.application)
    
    def run(self):
        self.socketio.run(app=self.application, port="8080")