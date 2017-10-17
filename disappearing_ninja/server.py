from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'very secret form'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def show_ninjas():
    return render_template("ninja.html")

@app.route('/ninja/<color>')
def show_ninjas_option(color):
    return render_template("ninja.html", color=color)



app.run(debug=True)
