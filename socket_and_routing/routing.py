from packages.flaskPackages import *
from service._init_ import *
import init
import utilities.globals as globals
application = init.application

@application.route('/', methods = ['GET'])
def index():
    serv_obj = IpDetailsServ()
    # if request.remote_addr not in globals.active:
    boolean, msg = serv_obj.insert(request.remote_addr)
    if boolean:
        globals.active.append(request.remote_addr)
        return render_template('dashboard.html', title="Talk To Strangers")
    else:
        return f"You are banned try again later"
    # else:
    #     return f"You have already one session open on your device."    
