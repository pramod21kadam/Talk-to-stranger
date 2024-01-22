from packages.packages import *
from model.master import *
class BannedIPDao:
    def getIP(ip_adderss):
        table = db.session.query(BannedIP).\
            filter(BannedIP.banned_ip == ip_adderss).\
            all()
        return table
