from flask import Blueprint, render_template, request, g

from .models.auth_register import User
from .models.posts import Posts
import random


bp_main = Blueprint('main', __name__)

def get_user(id):
    post_user = User.query.get_or_404(id)
    return post_user

@bp_main.route('/', methods=['GET', 'POST'])
def index():
    post = Posts.query.all()
    
    return render_template('index.html', post=post, get_user=get_user)
