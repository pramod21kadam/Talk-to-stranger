from model.master import *
from dao._init_ import *
import src.init as init
import utilities.globals as Global

sock = init.socketio

class ReportBotServ():
    def report(self, data):
        try:
            ip = IpDetailsDao.queryAll(data['ip'])
            by = IpDetailsDao.getIndex(request.remote_addr)
            if BotReportDao.getCount(by[0]) < 3:
                bot_report_obj = BotReport( ip.id, by[0], datetime.now())
                if base.insert(bot_report_obj):
                    base.commit()
                    if self.ban_ip(ip):
                        sock.emit('reload', room = ip.sid)
                    return True, ""
                return False, str("Error while insertion")
            else:
                return False, str("Limit exceded. Try after some time")
        except Exception as error:
            return False, str(error)

    def ban_ip(self, ip):
        try:
            if BotReportDao.getRepCount(ip.id) > 20:
                bann_obj = BannedIP(ip.ip_address, datetime.now(), datetime.now() - timedelta(hours=24*5))
                if base.insert(bann_obj):
                    base.commit()
                    Global.banned_ip.insert(0, ip)
                    return True
            return False
        except Exception as error:
            print(error)
            return False