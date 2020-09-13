from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class ArrivalPickup(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), nullable=False)
    arrival_pickup_status = db.Column(db.Integer, nullable=False)
    date = db.Column(db.Date, nullable=False)