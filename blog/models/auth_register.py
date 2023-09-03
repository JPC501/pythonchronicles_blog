from . import db


class User(db.Model):
    __tablename__='user_data'
    
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50),unique=True, nullable=False)
    email = db.Column(db.String(50), nullable=False)
    password = db.Column(db.Text, nullable=False)
    photo = db.Column(db.String(200))
    github_url = db.Column(db.String(200))
    twitter_url = db.Column(db.String(200))
    personal_website = db.Column(db.String(200))
    
    posts = db.relationship('Posts', backref='user', lazy=True)
    
    def __str__(self):
        return self.name
    
    def __init__(self, name, email, password, photo=None):
        self.name = name
        self.email = email
        self.password = password
        self.photo = photo