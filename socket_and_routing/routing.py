from packages.flaskPackages import *
import init

app = init.app

@app.route('/', methods = ['GET'])
def index():
    return render_template('dashboard.html', title="Talk To Strangers")