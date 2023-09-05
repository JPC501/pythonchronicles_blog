from flask import Blueprint, render_template, redirect
from .auth import login_required


bp_post = Blueprint('post', __name__, url_prefix='/post')

#create posts
@bp_post.route('/create_post', methods=['GET', 'POST'])
@login_required
def create_post():
    return render_template('create_post.html')