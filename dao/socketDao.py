from packages.packages import *
from model.master import *

class SocketDao:
    def query_all():
        table = db.session.query(ConnectionDetails).all()
        return table
    
    def searchIp(ip):
        try:
            table = db.session.query(ConnectionDetails).\
                filter(ConnectionDetails.ip_address == ip).\
                all()
            return table
        except Exception as err:
            print(f"Error in SocketDao search {err}")

    def disconnect(ip):
        table = db.session.query(ConnectionDetails).\
                filter(ConnectionDetails.ip_address == ip).all()
        return table