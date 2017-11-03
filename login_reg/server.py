from flask import Flask, request, redirect, render_template, session, flash
import re
import datetime
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'loginsdb')
def isValidEmail(email):
 if len(email) > 7:
     if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email) != None:
         return True
         return False

@app.route('/')
def index():
    return "hit index route"

@app.route('/registration', methods=["POST"])
def registration:
    return "hit registration route"

@app.route('/login', methods=["POST"])
    return "hight login route"

@app.route('/success')
    return "hit success route"



app.run(debug=True)
