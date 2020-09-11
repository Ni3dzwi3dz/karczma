# -*- coding: utf-8 -*-
from karczma import db, login
from datetime import datetime
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

#Contains classes - models for the db

#User
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True)
    email = db.Column(db.String(200), unique=True)
    password_hash = db.Column(db.String(100))

    def __repr__(self):
        return f'{self.username}'

    def generate_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))


#Session
class Session(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    title = db.Column(db.Text, nullable = False)
    user = db.Column(db.Integer)
    system = db.Column(db.Text)
    description = db.Column(db.Text)
    max_players = db.Column(db.Integer)
    dates = db.Column(db.Text)
    date_added = db.Column(db.DateTime, default=datetime.utcnow())

    def __repr__(self):
        return f'"{self.title}" ({self.system})'

#Grade

#Comment