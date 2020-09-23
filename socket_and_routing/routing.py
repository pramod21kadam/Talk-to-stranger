from packages.flaskPackages import *
import init

application = init.application

@application.route('/', methods = ['GET'])
def index():
    if "manager_1234" in request.args and request.args["manager_1234"] == "123@Iron":
        return render_template('manage.html', title="Manager")
    return render_template('dashboard.html', title="Talk To Strangers")
