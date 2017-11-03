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
    if "id" in session.keys():
        return redirect('/success')
    print "hit index route"
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    print "hit register route"
    first_name = request.form['first_name']
    last_name = request.form['last_name']
    email = request.form['email']
    pwd = request.form['password']
    pwdc = request.form['passwordc']
    valid = True
    errors = []
    pw_hash = bcrypt.generate_password_hash(pwd)
    if first_name == "" or isNotLongerThan2(first_name) == True:
        flash('First name cannot be empty')
        print "first name is empty"
        valid = False

    if last_name == "":
        flash('Last name cannot be empty')
        print "last name is empty"
        valid = False
    elif isNotLongerThan2(last_name) == True:
        flash('Last name must be longer than 2 characters')
        print "last name must be more than 2 chars"
        valid = False

    if email == "":
        flash('email is empty')
        print 'email is empty'
        valid = False
    elif not isValidEmail(email) == True:
        flash('not valid email')
        print 'not valid email'
        valid = False

    if len(pwd) < 8:
        flash('password is less than 8 characters')
        print 'not valid pwd'
        valid = False

    if pwd != pwdc:
        flash('Passwords dont match')
        print "passwords dont match"
        valid = False

    if valid:
        query = "INSERT INTO logins (first_name, last_name, email, password) VALUES (:first_name, :last_name, :email, :password)"
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': pw_hash
        }
        flash("You've inserted into the database!")
        mysql.query_db(query, data)
    else:
        flash("There was an error. You're registration did not go through.")

    print("{} {} {} {} {}".format(first_name, last_name, email, pwd, pwdc))
    flash("The world is brighter! You've registered!")
    return redirect('/')
@app.route('/login', methods=['POST'])
def login():
    if not isValidEmail(request.form['email']) == True:
        flash('not valid email')
        print 'not valid email'
    else:
        email = request.form['email']

    if len(request.form['password']) < 8:
        flash('password is less than 8 characters')
        print 'not valid pwd'
    else:
        password = request.form['password']

    query = "SELECT * FROM logins WHERE email=:email LIMIT 1"
    data = {
        "email": email,
        "password": password
    }

    user = mysql.query_db(query, data)
    print user
    print user[0]['password']
    # if len(user) == 0:
    #     flash("hey this isn't a real username")
    #     return redirect('/')
    # else:
    if bcrypt.check_password_hash(user[0]['password'], password):
        session["id"] = user[0]["id"]
        return redirect('/success')
    else:
        flash("invalid password")
        return redirect('/')


@app.route('/success')
def success():
    print "HIT SUCCESS!!!!!!!!!!!!!!!!"
    query = "SELECT * FROM logins WHERE id=:userid"
    data = {
        "userid": session["id"]
    }
    logged_user = mysql.query_db(query, data)[0]
    print logged_user
    return ("Hello {}! Your email is {}. Thank you for logging in.".format(logged_user["first_name"], logged_user["email"]))
    # flash("woohoo logged in!")
    # return redirect('/')
@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')
app.run(debug=True)
