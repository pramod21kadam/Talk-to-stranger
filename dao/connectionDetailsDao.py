from packages.packages import *
from model.master import *

class ConnectionDetailsDao:
   def queryAll(id):
      table = db.session.query(ConnectionDetails).\
         filter(ConnectionDetails.ip_address_index == id).\
         order_by(ConnectionDetails.id.desc()).\
         limit(1).\
         first()
      return table