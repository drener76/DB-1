# -*- coding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://scott:tiger@localhost/mydatabase'
db = SQLAlchemy(app)

class Peeple(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), unique=True)
    surname = db.Column(db.String(80), unique=True)
    patronymic = db.Column(db.String(50), unique=True)

    def __init__(self, name, surname, patronymic):
        self.name = name
        self.surname = surname
        self.patronymic = patronymic

    def __repr__(self):
        return '<Peeple %r>' % self.name

class Student(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    number = db.Column(db.Integer, unique=True)# номер число или строка?
    group = db.Column(db.Integer, unique=True)# не юник а внешний ключ

##
import sqlalchemy
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey


engine =  create_engine('postgresql://scott:tiger@localhost/mydatabase')
#engine =  create_engine('sqlite:///memrory:')

metadata = MetaData()
students = Table('student', metadata,
    Column('id', Integer, primary_key=True),
    Column('name1', String(50)),
    Column('name2', String(50)),
    Column('name3', String(50)),
    #Column('people_id', ForeignKey('people.id'))
)
people = Table('people', metadata,
    Column('id', Integer, primary_key=True),
    Column('name1', String(50)),
    Column('name2', String(50)),
    Column('name3', String(50)),
)

#create tables
metadata.create_all(engine)

#open connection
conn = engine.connect()

#insert
ins_test = students.insert().\
    values(name1='1', name2='2',name3='3',)

#results = conn.execute(people.insert(), [
#{'sdf_id':1, 'name1':'sdfsdf'}
#{...}
# ])
#
result = conn.execute(ins_test)
result.inserted_primary_key

print(str(ins_test))
ins_test.compile().params


#update
smthing = students.update().where(students.name1 == "sdfwe").values(name1='phahaha')
result = conn.execute(smthing)
result.rowcount

#delete
result = conn.execute(students.delete().where(students.name =='Terrry'))
result.rowcount

#select
s = select ([students.name1])
result = conn.execute(s)
for row in result:
    print(row)

'''
table object
students.colums.items()
[
('id', Column(('id',Integer(), table=students, primary_key=True... )))
('name',)
]
'''