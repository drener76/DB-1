# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#создать БД, postgresql://testBD:55Lqkk3@localhost/mydatabase_name
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:55Lqkk3@localhost/first'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#без db. префикса как-то можно?
class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    email = db.Column(db.String(120), unique=True)

    def __init__(self, name=None, email=None):
        self.name = name
        self.email = email

    def __repr__(self):
        return '<User %r>' % (self.name)

@app.route('/')
def index():
    User.__init__(name = "Vasya", email = "werwe")
    return "hi!"

if __name__ == "__main__":
    app.run