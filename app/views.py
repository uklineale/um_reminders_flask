from app import app

@app.route('/')
@app.route('/index')
def index():
    return "Urban Min is #1"
