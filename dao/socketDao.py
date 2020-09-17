from packages.packages import *
from model.master import *

class SocketDao:
    def query_all():
        table = db.session.query(ConnectionDetails).all()
        return table
    def disconnect(ip):
        table = db.session.query(ConnectionDetails).\
            filter(ConnectionDetails.ip_address == ip).\
            filter(ConnectionDetails.disconnect_time == None).all()
        return table[0]