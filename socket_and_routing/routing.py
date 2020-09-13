from packages.packages import *
from init import create_app
app = create_app()

@app.route('/', methods = ['GET'])
def index():
    return render_template('dashboard.html')