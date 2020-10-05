from packages.flaskPackages import *
from service._init_ import *
import init

application = init.application

@application.route('/', methods = ['GET'])
def index():
    serv_obj = IpDetailsServ()
    boolean, msg = serv_obj.insert(request.remote_addr)
    if boolean:
        return render_template('dashboard.html', title="Talk To Strangers")
    else:
        return f"You are banned till {msg}"
    
