from model.master import *
from dao._init_ import *
from utilities._init_ import *

class IpDetailsServ:
    def insert(self, ip):
        try:
            banned_table = BannedIPDao.getIP(ip)
            if banned_table:
                if datetime.now() > banned_table[-1].ban_till:
                    return True, "Unbanned"
                else:
                    return False, f"{banned_table[-1].ban_till}"
            else:
                ip_det_tabel = IpDetailsDao.queryAll(ip)
                if ip_det_tabel:
                    ip_det_tabel[-1].status = socket.connected.value
                    base.commit()
                    connDet_obj = ConnectionDetails(ip_det_tabel[-1].id, datetime.now())
                    if base.insert(connDet_obj):
                        base.commit()
                    return True, ""
                else:
                    ipDet_obj = IpDetails(ip)
                    if base.insert(ipDet_obj):
                        base.commit()
                    connDet_obj = ConnectionDetails(ip_det_tabel[-1].id, datetime.now())
                    if base.insert(connDet_obj):
                        base.commit()
                    return True, ""
        except Exception as error:
            print(error)
            return False, f"{error}"
        
    def disconnect(self, ip):
        try:
            index = IpDetailsDao.queryAll(ip)
            index[-1].status = socket.disconnected.value
            table = ConnectionDetailsDao.queryAll(index[-1].id)
            base.commit()
            if table:
                table.disconnect_time = datetime.now()
                base.commit()
                seconds = (table.disconnect_time - table.connect_time).total_seconds()
                # screentime remaining
                # index[-1].screen_time += seconds.time()
                # base.commit()
        except Exception as error:
            print(error)
            pass