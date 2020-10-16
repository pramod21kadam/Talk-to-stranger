from packages.flaskPackages import *
from model.master import *

class BotReportDao:
    def getCount(by_index):
        try:
            since = datetime.now() - timedelta(hours=24)
            count = db.session.query(func.count(BotReport.id)).\
                filter(and_(BotReport.time > since, BotReport.reported_by_index == by_index)).all()
            return count[0][0]
        except Exception as e:
            print("Error in BotReportDao: " + str(e))
            return False

    def getRepCount(id):
        try:
            since = datetime.now() - timedelta(hours=24)
            count = db.session.query(func.count(BotReport.id)).\
                filter(and_(BotReport.time > since, BotReport.reported_ip_index == id)).all()
            return count[0][0]
        except Exception as e:
            print("Error in BotReportDao: " + str(e))
            return -1