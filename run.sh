source myEnv.sh
gunicorn -k 'eventlet' -b 0.0.0.0:10041 build:app
