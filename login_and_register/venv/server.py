from flask import Flask, request, redirect, render_template, session, flash
import re
import datetime
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'loginsdb')
def isValidEmail(email):
 if len(email) > 7:
     if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email) != None:
         return True
         return False
def isString(string):
    if re.match("^[A-Za-z0-9_-]*$", string) != None:
        return True
        return False
def isNotLongerThan2(str):
    if len(str) < 2:
        return True
        return False
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    print "submitted form"
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    pwd = request.form['password']
    pwdc = request.form['passwordc']
    # run validations
    # pw_hash = Bcrypt.generate_password_hash(pwd)
    if isNotLongerThan2(first_name) == True:
        flash('First name must be longer than 2 characters')
        print 1
        return redirect('/')
    elif isNotLongerThan2(last_name) == True:
        flash('Last name must be longer than 2 characters')
        print 2
        return redirect('/')
    elif len(pwd) < 8:
        flash('Password is less than 8 characters')
        print 3
        return redirect('/')
    elif pwd is not pwdc:
        flash('Passwords dont match')
        print 4
        return redirect('/')
    elif isValidEmail(email) == True and isString(first_name) and isString(last_name) and (len(pwd) > 8) and (pwd == pwdc):
        print "This is a valid email address"
        print 5
        query = "INSERT INTO logins (first_name, last_name, email, password) VALUES (:first_name, :last_name, :email, :password)"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email'],
            'password': pw_hash
        }
        mysql.query_db(query, data)
        return render_template("success.html")
    else:
        print 6
        flash('Sorry there was an error')
        return redirect('/')




app.run(debug=True)
