from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func
from sqlalchemy import text

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    caretaker_id = db.Column(db.Integer, db.ForeignKey("caretaker.id"))
    caretaker = db.relationship("Caretaker", back_populates="user")

class Caretaker(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    name = db.Column(db.String(150))
    user = db.relationship("User", back_populates="caretaker")

class Status(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.String(150))
    severity = db.Column(db.Integer)
    stress = db.Column(db.Integer)
    light = db.Column(db.String(1))
    sound = db.Column(db.String(1))
    nausea = db.Column(db.String(1))
    aura = db.Column(db.String(1))
    visual = db.Column(db.String(1))
    dizzness = db.Column(db.String(1))
    fatigue = db.Column(db.String(1))
    unconcentrated = db.Column(db.String(1))
    neck = db.Column(db.String(1))
    user_id = db.Column(db.Integer, db.ForeignKey("user.id"))

