from packages.flaskPackages import *
from utilities.enums import *
import init
db = init.db

class ConnectionDetails(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False)
    ip_address = db.Column(db.String(20),primary_key=True, nullable = False)
    connect_time = db.Column(db.DateTime, nullable = False)
    disconnect_time = db.Column(db.DateTime, nullable = True)
    count = db.Column(db.Integer, nullable = False, default = 1)
    status = db.Column(db.String(1), nullable=False)

    def __init__(self, ip_address, connect_time, status = socket.connected.value, count = 1):
        self.ip_address = ip_address
        self.connect_time = connect_time
        self.status = status
        self.count = 1

db.create_all()