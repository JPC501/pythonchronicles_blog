from . import db

class User(db.Model):
    __tablename__='user_data'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),unique=True, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.String(500), nullable=False)
    photo = db.Column(db.String(200))
    
    def __str__(self):
        return self.name
    
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password