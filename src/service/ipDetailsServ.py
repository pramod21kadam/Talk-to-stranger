from model.master import *
from dao._init_ import *
from utilities._init_ import *

class IpDetailsServ:
    def insert(self, ip):
        try:
            banned_table = BannedIPDao.getIP(ip)
            if banned_table:
                if datetime.now() > banned_table[-1].ban_till:
                    ip_det_tabel = IpDetailsDao.queryAll(ip)
                    if ip_det_tabel:
                        ip_det_tabel.status = socket.connected.value
                        base.commit()
                        connDet_obj = ConnectionDetails(ip_det_tabel.id, datetime.now())
                        if base.insert(connDet_obj):
                            base.commit()
                        return True, ""
                    else:
                        ipDet_obj = IpDetails(ip)
                        if base.insert(ipDet_obj):
                            base.commit()
                        connDet_obj = ConnectionDetails(ipDet_obj.id, datetime.now())
                        if base.insert(connDet_obj):
                            base.commit()
                        return True, ""
                else:
                    return False, f"{banned_table[-1].ban_till}"
            else:
                ip_det_tabel = IpDetailsDao.queryAll(ip)
                if ip_det_tabel:
                    ip_det_tabel.status = socket.connected.value
                    base.commit()
                    connDet_obj = ConnectionDetails(ip_det_tabel.id, datetime.now())
                    if base.insert(connDet_obj):
                        base.commit()
                    return True, ""
                else:
                    ipDet_obj = IpDetails(ip)
                    if base.insert(ipDet_obj):
                        base.commit()
                    connDet_obj = ConnectionDetails(ipDet_obj.id, datetime.now())
                    if base.insert(connDet_obj):
                        base.commit()
                    return True, ""
        except Exception as error:
            print(error)
            return False, f"{error}"
        
    def disconnect(self, ip):
        try:
            ip_table = IpDetailsDao.queryAll(ip)
            ip_table.status = socket.disconnected.value
            table = ConnectionDetailsDao.queryAll(ip_table.id)
            table.disconnect_time = datetime.now()
            time_delta = (table.disconnect_time - table.connect_time)
            if not ip_table.screen_time:
                ip_table.screen_time = time_delta
            else:
                ip_table.screen_time += time_delta
            base.commit()
        except Exception as error:
            print(error)
            pass

    def update(self, sid, ip):
        try:
            ip_table = IpDetailsDao.queryAll(ip)
            ip_table.sid = sid
            base.commit()
            return True
        except Exception as error:
            print(error)
            return False