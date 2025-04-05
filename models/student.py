from utils.db import db

class Student(db.Model):


    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    gender = db.Column(db.String(255), nullable=False)
    previous_score = db.Column(db.Integer, nullable=False)
    current_score =  db.Column(db.Integer, nullable=False)
    attendance = db.Column(db.Integer, nullable=False)
    percentage = db.Column(db.Integer, nullable=False)