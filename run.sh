source /root/um_reminders/um_reminders_flask/myEnv.sh
/root/um_reminders/bin/gunicorn --pythonpath '/root/um_reminders/um_reminders_flask' -k 'eventlet' -b 0.0.0.0:10041 build:app > /root/um_reminders/um_reminders_flask/log.txt
