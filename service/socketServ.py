from packages.packages import *
from model.master import *
from dao._init_ import *

class SocketServ:
    def connect(self, ip_address):
        try:
            obj = ConnectionDetails(ip_address=ip_address, connect_time=datetime.now())
            if base.insert(obj):
                base.commit()
        except Exception as error:
            print(error)
    
    def disconnect(self, ip_address):
        try:
            record = SocketDao.disconnect(ip_address)
            record.disconnect_time = datetime.now()
            record.status = socket.disconnected.value
            return base.commit()
        except Exception as error:
            print(error)
        
        
