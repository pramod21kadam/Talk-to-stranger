from packages.flaskPackages import *

def create_app():
    application = Flask(__name__)
    
    socketio = SocketIO()
    application.config.from_pyfile('config.cfg')

    db = SQLAlchemy(app = application)
    from blueprints.api import api
    application.register_blueprint(api)
    socketio.init_app(application)
    return application, socketio, db

application, socketio, db = create_app()