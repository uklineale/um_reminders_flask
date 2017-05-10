#!um_reminders_flask/bin/python
import os
from app import app

def run():
    app.secret_key = os.urandom(30)
    app.run()

if __name__ == '__main__':
    run()
