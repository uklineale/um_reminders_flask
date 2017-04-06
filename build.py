#!um_reminders_flask/bin/python
import os
from app import app
app.secret_key = os.urandom(30)
app.run(debug=True)
