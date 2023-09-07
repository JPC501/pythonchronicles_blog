from flask import Blueprint, render_template, request, g

from .models.auth_register import User
from .models.posts import Posts


bp_main = Blueprint('main', __name__)


@bp_main.route('/', methods=['GET', 'POST'])
def index():
    
    post = Posts.query.all()
    
    return render_template('index.html', post=post)