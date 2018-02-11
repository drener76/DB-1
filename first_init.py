# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask import render_template

app = Flask(__name__)
#создать БД, postgresql://testBD:55Lqkk3@localhost/mydatabase_name
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:55Lqkk3@localhost/first'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

#без db. префикса как-то можно?

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

    def __init__(self, first_name, second_name, third_name, birthday, phone):
        self.first_name = first_name
        self.second_name = second_name
        self.third_name = third_name
        self.birthday = birthday
        self.phone = phone

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.first_name, self.second_name, self.third_name)


class Student(db.Model):
    __tablename__ = 'Student'
    id = db.Column(db.Integer, primary_key=True)
    faculty = db.Column(db.String(200))
    group = db.Column(db.String(30))#или числа?
    course = db.Column(db.String(30))#или числа?
    cart_number = db.Column(db.String(30))#Schema	public	normal
    date_introduction = db.Column(db.DateTime)

    #value = db.Column(db.String(30), unique=True)#узнать что такое "отметки"
    comment = db.Column(db.String(150))

    proforg = db.Column(db.Boolean)#поставить default=false
    event = db.Column(db.ForeignKey('Events.id'))#поставить default=false
    ticket = db.Column(db.ForeignKey('Tickets.id'))#поставить default=false

    def __init__(self, faculty, group, course):
        self.faculty = faculty
        self.group = group
        self.course = course

class Events(db.Model):
    __tablename__ = 'Events'
    id = db.Column(db.Integer, primary_key=True)
    name_event = db.Column(db.String(150))

class Tickets(db.Model):
    __tablename__ = 'Tickets'
    id = db.Column(db.Integer, primary_key=True)
    name_event = db.Column(db.String(150)) #foreign key
    date = db.Column(db.DateTime)

'''
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(80))
    body = db.Column(db.Text)
    pub_date = db.Column(db.DateTime)

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))
    category = db.relationship('Category',
        backref=db.backref('posts', lazy='dynamic'))

    def __init__(self, title, body, category, pub_date=None):
        self.title = title
        self.body = body
        if pub_date is None:
            pub_date = datetime.utcnow()
        self.pub_date = pub_date
        self.category = category

    def __repr__(self):
        return '<Post %r>' % self.title


class Category(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50))

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return '<Category %r>' % self.name
    '''

@app.route('/')
def index():
    #FL.__init__(first_name="Vasya", second_name="Vasya", third_name="Vasya", birthday="12.12.1222", phone="89091872397")
    #FL.__init__(first_name="test", second_name="xg", third_name="ert", birthday="12.12.1222", phone="23454657")
    return "hi!"

def init_FL():
    FL(first_name="Vas1ya", second_name="Vas1ya", third_name="Vas1ya", birthday="12.12.1222", phone="89091872397")
    FL(first_name="test", second_name="xg", third_name="ert", birthday="12.12.1222", phone="23454657")

@app.route('/FL')
def first_FL():
    return "hi!"

'''
@app.route('/post_user', methods=['POST'])
def first_FL():
    fl = FL(request.form['name_first'], request.form['name_second'], request.form['name_third'])
    db.session.add(fl)
    db.session.commit()
'''

if __name__ == "__main__":
    init_FL()

    #st1 = Student(faculty="вирусолог", group="sdf", course='123')
    fl = FL(first_name="Vasya", second_name="vasichkin", third_name='sdfe', birthday="12.12.1222", phone="234d24345-9")
    fl3 = FL(first_name="Vasya2", second_name="vasichkin2", third_name='sdf234e', birthday="12.12.1222", phone="43243459")

    fl2 = FL(first_name="1", second_name="2", third_name="3", birthday="12.12.1222", phone="89918235397")
    #fl = FL(request.form['name_first'], request.form['name_second'], request.form['name_third'])
    db.session.add(fl)
    db.session.add(fl2)
    db.session.add(fl3)
    #db.session.add(st1)
    db.session.commit()

    app.run