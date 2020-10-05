from packages.flaskPackages import *
from utilities.enums import *
import init
db = init.db

class IpDetails(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False)
    ip_address = db.Column(db.String(20), primary_key=True, nullable = False)
    sid = db.Column(db.String(50), nullable=True)
    screen_time = db.Column(db.Time, nullable = True, default = "00:00:00")
    status = db.Column(db.String(1), nullable=False)

    def __init__(self, ip_address,status = socket.connected.value):
        self.ip_address = ip_address
        self.status = status

class ConnectionDetails(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False)
    ip_address_index = db.Column(db.Integer, nullable = False)
    connect_time = db.Column(db.DateTime, nullable = False)
    disconnect_time = db.Column(db.DateTime, nullable = True)

    def __init__(self, ip_address_index, connect_time):
        self.ip_address_index = ip_address_index
        self.connect_time = connect_time

class BotReport(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False)
    reported_ip_index = db.Column(db.Integer, nullable = False)
    time = db.Column(db.DateTime, nullable = False)
    reported_by_index = db.Column(db.Integer, nullable = False)

    def __init__(self, reported_ip, reported_by, time):
        self.reported_ip_index = reported_ip
        self.reported_by_index = reported_by
        self.time = time

class BannedIP(db.Model):
    id = db.Column(db.Integer, primary_key = True, autoincrement = True, nullable = False)
    banned_ip = db.Column(db.Integer, nullable = False)
    ban_time = db.Column(db.DateTime, nullable = False)
    ban_till = db.Column(db.DateTime, nullable = False)

    def __init__(self, banned_ip, ban_time, ban_till):
        self.banned_ip = banned_ip
        self.ban_time = ban_time
        self.ban_till = ban_till
        
db.create_all()