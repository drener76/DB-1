# -*- coding: utf-8 -*-
from sqlalchemy import create_engine
from sqlalchemy import Table, Column, Integer, String, MetaData, ForeignKey
from sqlalchemy.orm import mapper

engine = create_engine(
    "postgresql+pg5432://localhost/test",
    isolation_level="READ UNCOMMITTED"
)

metadata = MetaData()
student_table = Table('student', metadata,
    Column('id', Integer, primary_key=True),
# ФИО    для sqlLite String для PostgreSQL или MySQL String(50)
    Column('name1', String(50)),
    Column('name2', String(50)),
    Column('name3', String(50)),
)

metadata.create_all(engine)

class Student(object):
    def __init__(self, name1, name2, name3):
        self.name1 = name1
        self.name2 = name2
        self.name3 = name3

    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name1, self.name2, self.name3)

mapper(Student, student_table)

student = Student('test', 'test', 'test3')  # это переменная


######### декларативное создание
from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()
class Student(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name1 = Column(String(50))
    name2 = Column(String(50))
    name3 = Column(String(50))

    def __init__(self, name1, name2, name3):
        self.name1 = name1
        self.name2 = name2
        self.name3 = name3
    def __repr__(self):
        return "<User('%s','%s', '%s')>" % (self.name1, self.name2, self.name3)

#В данном случае, создание таблицы User
Base.metadata.create_all(engine)


from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

session = Session()

vasiaStudent = Student("vasia", "Vasiliy Pypkin", "vasia2000")
session.add(vasiaStudent)

Session.configure(bind=engine)  # Как только у вас появится engine
session = Session()

