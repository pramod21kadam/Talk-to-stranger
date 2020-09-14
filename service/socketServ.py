from packages.packages import *
from model.master import *
from dao._init_ import *

class SocketServ:
    def getall(self):
        try:
            table = SocketDao.get()
            return table
        except Exception as e:
            print(e)
            return None
    
    def post(self):
        try:
            conn = ConnectionDetails()
            conn.ip = request.remote_addr
            conn.connection_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            conn.status = "A"
            # if base.insert(conn):
                # print("added")
                # base.commit()
            # print(db.session.add(conn))
            obj = Login()
            obj.email = " 1234@123.com"
            db.session.add(obj)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            print(f"socketServ POST Error:- {e}")
