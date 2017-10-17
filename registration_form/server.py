from flask import Flask, render_template, redirect, request, session, flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile('[^0-9]')
app = Flask(__name__)
app.secret_key = "ThisIsSecret!"


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    name = request.form['name']
    lastname = request.form['lastname']
    email = request.form['email']
    password = request.form['password']
    cpassword = request.form['cpassword']
    if len(name) < 1:
        flash("Name cannot be empty!")
    elif len(lastname) < 1:
        flash("Last name cannot be empty!")
    elif len(email) < 1:
        flash("Email cannot be empty!")
    elif len(password) < 1:
        flash("Password cannot be empty!")
    elif len(cpassword) < 1:
        flash("You must confirm password!")
    elif not NAME_REGEX.match(name):
        flash("Invalid Name!")
    elif not NAME_REGEX.match(lastname):
        flash("Invalid Lastname!")
    elif not EMAIL_REGEX.match(email):
        flash("Invalid Email!")
    elif request.form['password'] != request.form['cpassword']:
        flash("Passwords don't match!")
    else:
        flash("Success!")
    return redirect('/')

app.run(debug=True)
