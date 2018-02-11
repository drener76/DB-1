# -*- coding: utf-8 -*-
#from flask import Flask
#from flask_sqlalchemy import SQLAlchemy
#from app import main

from app import db
from datetime import datetime

#app = Flask(__name__)
#db = SQLAlchemy(app)

class FL(db.Model):
    __tablename__ = 'FL'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(50))
    second_name = db.Column(db.String(50))
    third_name = db.Column(db.String(50))
    birthday = db.Column(db.DateTime)
    phone = db.Column(db.String(16), unique=True)#форматировать на клиенте

    discont_card = db.Column(db.String(16), unique=True) #вроде бы 16 максимум
    adress_prop = db.Column(db.String(250))# подставлять ул, дом, на клиенте.. или отдельные поля.. удобней наверно отдельные поля
    adress_fact = db.Column(db.String(250))

    city = db.Column(db.String(100))
    street = db.Column(db.String(100))
    home = db.Column(db.String(50))

    email = db.Column(db.String(60), unique=True)

    def __init__(self, first_name, second_name, third_name, birthday,phone ,discont_card ,adress_prop ,adress_fact):
        self.first_name = first_name
        self.second_name = second_name
        self.third_name = third_name
        self.birthday = birthday
        self.phone = phone
        self.discont_card = discont_card
        self.adress_prop = adress_prop
        self.adress_fact = adress_fact

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.first_name, self.second_name, self.third_name)


class Student(db.Model):
    __tablename__ = 'Student'
    id = db.Column(db.Integer, primary_key=True)
    faculty = db.Column(db.String(200))
    group = db.Column(db.String(30))#или числа?
    course = db.Column(db.String(30))#или числа?
    cart_number = db.Column(db.String(30))
    date_in_prof = db.Column(db.DateTime)
    date_in_univers = db.Column(db.DateTime)

    comment = db.Column(db.String(150))
    proforg = db.Column(db.Boolean)#поставить default=false

    event = db.Column(db.ForeignKey('Events.id'))#поставить default=false
    ticket = db.Column(db.ForeignKey('Tickets.id'))#поставить default=false
    FL = db.Column(db.ForeignKey('FL.id'))#как записать данные с 1й формы в 2 таблицы

    def __init__(self, faculty, group, course, cart_number, date_in_prof, date_in_univers , comment, proforg):
        self.faculty = faculty
        self.group = group
        self.course = course
        self.cart_number = cart_number
        self.date_in_prof = date_in_prof
        self.date_in_univers = date_in_univers
        self.comment = comment
        self.proforg = proforg

class Events(db.Model):
    __tablename__ = 'Events'
    id = db.Column(db.Integer, primary_key=True)
    name_event = db.Column(db.String(150))

class Tickets(db.Model):
    __tablename__ = 'Tickets'
    id = db.Column(db.Integer, primary_key=True)
    name_event = db.Column(db.String(150)) #foreign key
    date = db.Column(db.DateTime)

class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(50))
    password = db.Column(db.String(25))