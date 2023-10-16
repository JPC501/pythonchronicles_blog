from . import db
from datetime import datetime


class Posts(db.Model):
    __tablename__ = 'posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    content_post = db.Column(db.Text)
    info = db.Column(db.Text)
    author = db.Column(db.Integer, db.ForeignKey('user_data.id'),
                       nullable=False)
    url = db.Column(db.String(200), unique=True, nullable=False)
    created = db.Column(db.Date, nullable=False, default=datetime.utcnow)

    def __str__(self):
        return self.title

    def __init__(self, author, title,
                 content_post, info, url, created):
        self.author = author
        self.title = title
        self.content_post = content_post
        self.info = info
        self.url = url
        self.created = created if created is not None else datetime.utcnow()
