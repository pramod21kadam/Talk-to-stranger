from packages.flaskPackages import *

def create_app():
    app = Flask(__name__)
    
    socketio = SocketIO()
    app.config.from_pyfile('config.cfg')

    db = SQLAlchemy(app = app)
    from blueprints.api import api
    app.register_blueprint(api)
    socketio.init_app(app)
    return app, socketio, db

app, socketio, db = create_app()