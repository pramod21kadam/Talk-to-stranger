from packages.packages import *
from model.master import *

class SocketDao:
    def get():
        table = db.session.query(ConnectionDetails).all()
        return table
    