from flask import Flask, render_template, request, redirect, session, flash
app = Flask(__name__)
app.secret_key = 'very secret form'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/process', methods=["POST"])
def result():
    if len(request.form['name']) < 1:
        flash("Name cannot be empty!") # just pass a string to the flash function
    elif len(request.form['location']) < 1:
        flash("Location cannot be empty!") # just pass a string to the flash function
    elif len(request.form['language']) < 1:
        flash("Language cannot be empty!")
    else:
        flash("Success! Your name is {} at location {} and favorite language {}".format(request.form['name'], request.form['location'], request.form['language']))
    return redirect('/')
    # name = request.form['name']
    # location = request.form['location']
    # language = request.form['language']
    # comment = request.form['comment']

    # return render_template('result.html')

app.run(debug=True)
