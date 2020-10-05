from .api import api
import init
init.application.register_blueprint(api, url_prefix='/api')