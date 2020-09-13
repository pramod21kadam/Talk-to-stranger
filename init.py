from flask import Flask
from flask_socketio import SocketIO

socketio = SocketIO()

def create_app(debug=False):
    app = Flask(__name__)
    app.debug = debug
    app.config.from_pyfile('config.cfg')

    from blueprints.api import api
    app.register_blueprint(api)

    socketio.init_app(app)
    return app