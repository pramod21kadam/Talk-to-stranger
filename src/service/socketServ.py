from packages.packages import *
# from model.master import *
from dao._init_ import *

class SocketServ():
    def connect(self, ip_address):
        try:
            result = SocketDao.searchIp(ip_address)
            if len(result) == 0:
                obj = ConnectionDetails(ip_address=ip_address, connect_time=datetime.now())
                if base.insert(obj):
                    return base.commit(), "successfully inserted"
            else:
                result = result[0]
                result.count += 1
                result.connect_time = datetime.now()
                result.status = socket.connected.value
                return base.commit(), "successfully inserted"
        except Exception as error:
            print(f"Error:\t in SocketServ Connect {error}")
            return False, error
    
    def disconnect(self, ip_address):
        try:
            record = SocketDao.disconnect(ip_address)

            if len(record) != 0:
                record[0].disconnect_time = datetime.now()
                record[0].status = socket.disconnected.value
                return base.commit()
            return False, "successfully inserted"
        except Exception as error:
            print(error)
            return False, error
        
    def getAll():
        try:
            return True, SocketDao.query_all()
        except Exception as error:
            print(f"Error in socketServ.get {error}")
            return False, None
        
