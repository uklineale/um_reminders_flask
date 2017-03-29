from flask import render_template, request, flash, redirect
import csv_parser
from app import app

ALLOWED_EXTENSIONS = set(['csv'])

def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET','POST'])
def upload():
    if request.method == 'POST':
        csv = request.files['file']

        if csv.filename == '':
            flash('No selected file')
            return redirect(request.url)

        #Request file is a file stream, must be read
        #Read returns bytes, needs to be converted to string
        csv_string = csv.read().decode('utf-8')

        calls = csv_parser.parseCsv(csv_string)

        flash("Data from controller after parsing: ")
        for number in calls['phone']:
            flash(number)
        
        return render_template('upload.html')
    else:
        return render_template('upload.html')
