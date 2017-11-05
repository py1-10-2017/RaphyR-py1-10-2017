from flask import Flask, request, redirect, render_template, session, flash
import re
import datetime
import time
from mysqlconnection import MySQLConnector
from flask_bcrypt import Bcrypt
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
bcrypt = Bcrypt(app)
mysql = MySQLConnector(app,'the_wall')
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
        print "print id is in session keys"
        # return redirect('/success')
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
        query = "INSERT INTO users (first_name, last_name, email, password, created_at, updated_at) VALUES (:first_name, :last_name, :email, :password, NOW(), NOW())"
        data = {
            'first_name': first_name,
            'last_name': last_name,
            'email': email,
            'password': pw_hash,
        }
        flash("The world is brighter! You've registered!")
        mysql.query_db(query, data)
    else:
        flash("There was an error. You're registration did not go through.")

    print("{} {} {} {} {}".format(first_name, last_name, email, pwd, pwdc))
    return redirect('/')
@app.route('/login', methods=['POST'])
def login():
    print "HIT LOGIN!!!!!"
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

    query = "SELECT * FROM users WHERE email=:email LIMIT 1"
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
        session["first_name"] = user[0]["first_name"]
        session["last_name"] = user[0]["last_name"]
        print str(session["id"]) + " " + session["first_name"] + " "  + session["last_name"]
        return redirect('/wall')
    else:
        flash("invalid password")
        return redirect('/')

@app.route('/wall')
def success():
    print "HIT SUCCESS!!!!!!!!!!!!!!!!"
    query = "SELECT messages.id as msg_id, users.id, users.first_name, users.last_name, message as message, messages.created_at as messages_created FROM messages JOIN users on users.id = messages.user_id ORDER BY messages.created_at DESC"
    # query = "SELECT * FROM users"
    messages = mysql.query_db(query)
    print messages

    comnts_query = "SELECT message_id, messages.id, first_name, last_name, comment, comments.created_at as comment_created FROM comments JOIN messages on messages.id =comments.message_id JOIN users on users.id = comments.user_id"
    # query = "SELECT * FROM users"
    comments = mysql.query_db(comnts_query)
    print "these are all the comments"
    print comments

    return render_template('wall.html', messages=messages, comments=comments)

@app.route('/message', methods=['POST'])
def create():
    print "hit message"
    query = "INSERT into messages (message, user_id, created_at, updated_at) VALUES (:message, :id, NOW(), NOW())"
    data = {
        "message": request.form['message'],
        "id": session["id"]
    }
    userMessage = mysql.query_db(query, data)
    # print "========================= this is the user message on the form ========================= "
    # print userMessage
    return redirect('/wall')
@app.route('/message/<msg_id>/comment', methods=['POST'])
def createComment(msg_id):
    print "hit comment"
    query = "INSERT INTO comments (user_id, message_id, comment, created_at, updated_at) VALUES (:id, :msgid, :comment, timestampdiff(minute,messages.created_at, NOW())"
    data = {
        "id": session["id"],
        "msgid": msg_id,
        "comment": request.form['comment'],
        "now": time.strftime("%m-%d %H:%M")
    }
    comments = mysql.query_db(query, data)
    print "posted comment on db"
    return redirect('/wall')
@app.route('/logout')
def logout():
    session.clear()
    flash('You have logged out')
    return redirect('/')
app.run(debug=True)
