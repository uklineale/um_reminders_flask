from flask.ext.login import UserMixin

class User(UserMixin):
    def __init__(self, name, id):
        self.id = id
        self.name = name
        
