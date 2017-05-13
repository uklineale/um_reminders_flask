#!um_reminders_flask/bin/python
import os
from app import app

if __name__ == '__main__':
    app.secret_key = os.urandom(30)
    app.run()
