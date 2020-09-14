from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class ConnectionDetails(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    ip = db.Column(db.String(20), nullable = False)
    connection_time = db.Column(db.DateTime, nullable=False)
    disconnection_time = db.Column(db.DateTime, nullable=True)
    status = db.Column(db.String(1), nullable = False)

class Login(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    email = db.Column(db.String(20), nullable = False)