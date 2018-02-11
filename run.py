#!flask/bin/python
from flask import Flask
from app import app
app.run(debug = True)


app = Flask(__name__)