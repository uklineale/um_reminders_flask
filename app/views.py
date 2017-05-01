from os import environ
from flask import render_template, request, flash, redirect, session
from passlib.hash import argon2
from app.classes import um_parser,um_messenger
from app import app

ALLOWED_EXTENSIONS = set(['csv'])
UM_PASSWORD = argon2.hash(environ["UM_PASSWORD"])

### Private methods ###

# Handles the sanitized request by parsing the csv
# Sends out messages to each number. You can see the
# texts that were sent on the page after.
# 
# Params:
#   request - the http request coming in from the form
#       in upload.html
# Return:
#   the http response
def handleCsv(request):
    csv = request.files['file']

    print("Got file sucessfully")
    if csv.filename == '':
        flash('No selected file')
        return redirect(request.url)

    #Request file is a file stream, must be read
    #Read returns bytes, needs to be converted to string
    csv_string = csv.read().decode('utf-8')

    calls = um_parser.parseCsv(csv_string)

    flash("Data from controller after parsing: ")
    for line in calls:
        flash(line)
        um_messenger.sendMessage(line[0], line[1])
        
    return render_template('upload.html')

# Validates input file is allowed
# Params:
#   filename - string of the input file
# Return:
#   true if valid, false if not
def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

### Routes ###

@app.route('/', methods=['GET','POST'])
def upload():
    # Verify user is logged in
    if not session.get('logged_in'):
        return render_template('login.html')

    if request.method == 'POST':
        print("POST Request")
        return handleCsv(request)
    else:
        return render_template('upload.html')

@app.route('/login', methods=['POST'])
def login():
    try:
        if argon2.verify(request.form['password'], UM_PASSWORD):
            flash("Welcome")
            session['logged_in'] = True
            return render_template('upload.html')
        else:
            flash('Wrong password.')
            return render_template('login.html')
    except KeyError:
        flash('Password not set in environment variables. See the Setting Up section of the documentation')
        return render_template('login.html')
