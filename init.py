from packages.flaskPackages import *
import utilities.globals as Global
from socket_and_routing.sockets import SocketNameSpace

def create_app():
    application = Flask(__name__)
    
    socketio = SocketIO()
    socketio.on_namespace(SocketNameSpace('/'))
    application.config.from_pyfile('config.cfg')

    # db = SQLAlchemy(app = application)

    from blueprints.api import api
    application.register_blueprint(api, url_prefix='/')
    
    socketio.init_app(application)
    return application, socketio

application, socketio = create_app()