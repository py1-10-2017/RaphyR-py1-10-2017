from flask import Flask, request, redirect, render_template, session, flash
import re
import datetime
from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
mysql = MySQLConnector(app,'full_friends')
def isValidEmail(email):
 if len(email) > 7:
     if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email) != None:
         return True
         return False

@app.route('/')
def index():
    print "got index"
    query = "SELECT * FROM friends"
    allfriends = mysql.query_db(query)
    return render_template('index.html', friends=allfriends)

@app.route('/friends', methods=['POST'])
def create():
    print "submitted form"
    formEmail = request.form['email']
    print formEmail
    if (isValidEmail(formEmail) == True):
        print "This is a valid email address"
        query = "INSERT INTO friends (first_name, last_name, email, created_at, updated_at) VALUES (:first_name, :last_name, :email, NOW(), NOW())"
        data = {
            'first_name': request.form['first_name'],
            'last_name': request.form['last_name'],
            'email': request.form['email']
        }
        mysql.query_db(query, data)
        allfriends = mysql.query_db("SELECT * FROM friends")
        return render_template("index.html", friends=allfriends)
    else:
        print "This is not a valid address"
        flash('This is not a valid email!')
        return redirect('/')


@app.route('/friends/<id>/edit')
def edit(id):
    print "went through to edit"
    # Write query to select specific user by id. At every point where
    # we want to insert data, we write ":" and variable name.
    friends = mysql.query_db("SELECT * FROM friends WHERE id = {}".format(id))[0]
    return render_template('edit.html', one_friend=friends)


@app.route('/friends/<id>', methods=['POST'])
def update(id):
    print "went through"
    # Write query to select specific user by id. At every point where
    # we want to insert data, we write ":" and variable name.
    query = "UPDATE friends SET first_name=:updated_fname, last_name=:updated_lname, email=:updated_email, updated_at=NOW() WHERE id=:friend_id"
    # Then define a dictionary with key that matches :variable_name in query.
    data = {
        'friend_id': id,
        'updated_fname': request.form['first_name'],
        'updated_lname': request.form['last_name'],
        'updated_email': request.form['email'],
    }
    # Run query with inserted data.
    mysql.query_db(query, data)
    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template under alias one_friend.
    return redirect('/')

@app.route('/friends/<id>/delete')
def destroy(id):
    print "delete went through"
    print id
    # Write query to select specific user by id. At every point where
    # we want to insert data, we write ":" and variable name.
    query = "DELETE FROM friends WHERE id=:friend_id"
    # Then define a dictionary with key that matches :variable_name in query.
    data = {'friend_id': id}
    # Run query with inserted data.
    mysql.query_db(query, data)
    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template under alias one_friend.
    return redirect('/')
app.run(debug=True)
