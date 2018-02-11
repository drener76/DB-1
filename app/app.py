# -*- coding: utf-8 -*-
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask import render_template, request, redirect, url_for

app = Flask(__name__)
'''
# configuration
DATABASE = 'flaskr.db'
DEBUG = True
SECRET_KEY = 'my_precious'
USERNAME = 'admin'
PASSWORD = 'admin'
'''

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:55Lqkk3@localhost/first'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from model import *

@app.route('/')
def index():  #TODO сверстать главную страницу
    #хз как это сделать.. нажали кнопку. нас должно перекинуть на шаблон student

    myFL = FL.query.all()
    Item = FL.query.filter_by(first_name="test").first()

    st = request.form['stud']
    if st:
        return render_template('student.html')
    #return render_template('index.html')
    return render_template('index.html', myFL=myFL, Item=Item )


@app.route('/post_fl', methods=['POST'])
def post_fl():
    fl = FL(request.form['first_name'], request.form['second_name'], request.form['third_name'])
    db.session.add(fl)
    db.session.commit()
    return redirect(url_for('index'))


@app.route('/post_student', methods=['POST'])
def post_student():
    fl = FL (request.form['first_name'],
             request.form['second_name'],
             request.form['third_name'],
             request.form['birthday'],
             request.form['phone'],#порядок не тот
             request.form['adress_prop'],
             request.form['adress_fact'],
             request.form['discont_card'],
             request.form['email']
             )
    st = Student (
                  request.form['faculty'],
                  request.form['group'],
                  request.form['course'],
                  request.form['cart_number'],
                  request.form['date_in_prof'],
                  request.form['date_in_univers'],
                  request.form['comment'],
                  request.form['proforg']
                  )

#как разрешится добавление?
    db.session.add(fl)
    db.session.add(st)
    db.session.commit()
    #return render_template('add_people.html')
    return redirect(url_for('index'))



def add_student():
    p1 = 'sdf1'
    p2 = 'sdf2'
    p3 = 'sdf3'#фио
    p4 = '123-43-657-'#card prof
    p5 = '11.12.2000'#birthday
    p6 = '9may street-'#adresprop
    p7 = '9may street-'#adresfact
    p8 = '8904569'#phone
    p9 = 'it pritty '#comment
    p10 = '01.09.2009'#into univers
    p11 = '01.10.2009'#into prof
    p12 = '5'#cours
    p13 = 'fizio'#faculty
    p14 = '2'#group
    p15 = '213432443'#diskont card
    p16 = '223@mail'#email
    p17 = 'true'#proforg

#не все выводится..
    temp1= FL(
        first_name=p1,
        second_name=p2,
        third_name=p3,
        birthday=p5,
        phone=p8,
        discont_card=p15,
        adress_prop=p6,
        adress_fact=p7
    )
    temp2= Student(
        faculty = p13,
        group = p14,
        course = p12,
        cart_number = p4,
        date_in_prof = p11,
        date_in_univers = p10,
        comment = p9,
        proforg = p17
    )

    #db.session.add(temp1)
    #db.session.add(temp2)
    db.session.commit()
    return 1
    #return redirect(url_for('index'))

def init_FL():
    FL(first_name="Vas1ya", second_name="Vas1ya", third_name="Vas1ya", birthday="12.12.1222", phone="89091872397")
    FL(first_name="test", second_name="xg", third_name="ert", birthday="12.12.1222", phone="23454657")


if __name__ == "__main__":
    #init_FL()
    add_student()

    #st1 = Student(faculty="вирусолог", group="sdf", course='123')
    #fl = FL(first_name="1", second_name="2", third_name='3')#, birthday="31.12.1222", phone="1")
    #fl3 = FL(first_name="Vasya2", second_name="vasichkin2", third_name='sdf234e', birthday="12.12.1222", phone="43243459")

    #   fl2 = FL(first_name="1", second_name="2", third_name="3", birthday="12.12.1222", phone="89918235397")
    #fl = FL(request.form['name_first'], request.form['name_second'], request.form['name_third'])
    #db.session.add(fl)
    #db.session.add(fl2)
    #db.session.add(fl3)
    #db.session.add(st1)
    db.session.commit()

    app.run(debug=True)
    #app.run(host='0.0.0.0')




