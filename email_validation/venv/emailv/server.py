from flask import Flask, request, redirect, render_template, session, flash
import re
from mysqlconnection import MySQLConnector
from validate_email import validate_email
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"
mysql = MySQLConnector(app,'emaildb')
def isValidEmail(email):
 if len(email) > 7:
     if re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', email) != None:
         return True
         return False

@app.route('/')
def index():
    query = "SELECT * FROM email"
    email = mysql.query_db(query)
    return render_template('index.html', all_emails=email)

@app.route('/emails', methods=['POST'])
def create():
    formEmail = request.form['email']
    if (isValidEmail(formEmail) == True):
        print "This is a valid email address"
        query = "INSERT INTO email (email, created_at, updated_at) VALUES ('{}', NOW(), NOW())".format(formEmail)
        data = {
            'email': formEmail
        }
        mysql.query_db(query, data)
        selectEmails = mysql.query_db("SELECT * FROM email ORDER BY ID DESC LIMIT 1")
        allEmails = mysql.query_db("SELECT * FROM email")
        return render_template("success.html", emails=selectEmails, allemails=allEmails)
    else:
        print "This is not a valid address"
        flash('This is not a valid email!')
        return redirect('/')


@app.route('/emails/<id>')
def show(id):
    print "went through"
    # Write query to select specific user by id. At every point where
    # we want to insert data, we write ":" and variable name.
    query = "SELECT * FROM email WHERE id = :specific_id"
    # Then define a dictionary with key that matches :variable_name in query.
    data = {'specific_id': id}
    # Run query with inserted data.
    friends = mysql.query_db(query, data)
    # Friends should be a list with a single object,
    # so we pass the value at [0] to our template under alias one_friend.
    return render_template('success.html', one_email=email[0])

app.run(debug=True)
