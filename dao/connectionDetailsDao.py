from packages.packages import *
from model.master import *

class ConnectionDetailsDao:
   def queryAll(id):
      table = db.session.query(ConnectionDetails).\
         filter(ConnectionDetails.ip_address_index == id).\
         filter(ConnectionDetails.disconnect_time == None).\
         first()
      return table