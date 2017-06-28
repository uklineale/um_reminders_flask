#!um_reminders_flask/bin/python
import os
import logging
from app import app

def run():
    logging.basicConfig(filename='um.log', level=logging.INFO)
    app.secret_key = os.urandom(30)
    app.run()

if __name__ == '__main__':
    run()
