from os import environ
from flask import render_template, request, flash, redirect, session
from passlib.hash import argon2
from app.classes import um_parser,um_messenger
from app import app
from time import sleep
import logging
import csv

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
    csvFile = request.files['file']
    filename = csvFile.filename

    if filename == '' or not allowed_file(filename):
        flash('Invalid file')
        logging.info('Invalid file attempt of ' + filename)
        return redirect(request.url)

    logging.info("Got file " + filename)

    #Request file is a file stream, must be read
    #Read returns bytes, needs to be converted to string
    csv_string = csvFile.read().decode('utf-8')
    reader = csv.reader(csv_string.split('\n'), delimiter=',')
    logging.info("Starting to send messages")

    message_counter = 0
    for line in reader:
        print(len(line))
        if line[0] != "" and line[1] != "":
            logging.info("Sending message to " + line[0])
            message_id = um_messenger.sendMessage(line[0], line[1])
            message_counter += 1
            sleep(1) #not hit rate limit of 1 msg/s

    logging.info("Messages sent: " + str(message_counter))
    flash("Messages sent: " + str(message_counter))

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
        return handleCsv(request)
    else:
        return render_template('upload.html')

@app.route('/login', methods=['POST'])
def login():
    try:
        if argon2.verify(request.form['password'], UM_PASSWORD):
            logging.info("Successful login")
            flash("Welcome")
            session['logged_in'] = True
            return render_template('upload.html')
        else:
            logging.info("Failed password attempt")
            flash('Wrong password.')
            return render_template('login.html')
    except KeyError:
        flash('Password not set in environment variables. See the Setting Up section of the documentation')
        return render_template('login.html')

@app.route('/callback', methods=['GET','POST'])
def callback():
    return 'Callback OK'
