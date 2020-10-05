# from packages.packages import *
from utilities.enums import *
from model.master import *

class IpDetailsDao():
   def getIndex(ip):
      index = db.session.query(IpDetails.ip_address).\
      filter(IpDetails.ip_address == ip).one()
      return index
      
   def queryAll(ip):
      table = db.session.query(IpDetails).\
         filter(IpDetails.ip_address == ip).\
         all()
      return table