from flask import Flask, render_template, request, redirect, session
import random
random = random.randrange(0, 101)
app = Flask(__name__)
app.secret_key = 'very secret guess'

@app.route('/')
def index():
    # print guess
    # print random
    return render_template('index.html')

@app.route('/guess', methods=['POST'])
def guess():
    session['guess'] = int(request.form['number'])
    session['random'] = random
    print random
    #session['hundred'] = 100
    #session['random'] = random

    # if guess < 100:

    # print session['guess']
    return redirect('/')

@app.route('/reset', methods=['POST'])
def result():
    session.pop('guess')
    session.pop('random')
    return redirect('/')



app.run(debug=True)
