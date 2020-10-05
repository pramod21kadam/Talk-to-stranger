from model.master import *
from dao._init_ import *

class ReportBotServ():
    def report(self, data):
        try:
            ip = IpDetailsDao.getIndex(data['ip'])
            by = IpDetailsDao.getIndex(data['by'])
            bot_report_obj = BotReport( ip, by, datetime.now())
            if base.insert(bot_report_obj):
                base.commit()
                return True, ""
            return False, str("Error while insertion")
        except Exception as error:
            return False, str(error)
            pass