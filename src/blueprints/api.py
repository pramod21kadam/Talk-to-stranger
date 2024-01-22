from flask import Blueprint
from flask.views import MethodView
from controller._init_ import *

api = Blueprint('api', __name__, template_folder='templates')

def register_api(view, endpoint:str, url:str, pk:str='id', pk_type:str='int') -> None:
    print("registered api endpoint=%s url=%s" %(endpoint, url))
    view_func = view.as_view(endpoint)
    api.add_url_rule(url, defaults={pk: None}, view_func=view_func, methods=['GET', 'PATCH', 'PUT', 'DELETE'])
    api.add_url_rule(url, view_func=view_func, methods=['POST', 'OPTIONS'])
    api.add_url_rule('%s<%s:%s>' % (url, pk_type, pk), view_func=view_func, methods=['GET', 'PATCH', 'PUT', 'DELETE'])

register_api(HomeController, '/', '/')