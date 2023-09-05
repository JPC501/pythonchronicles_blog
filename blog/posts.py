from flask import Blueprint, render_template, redirect


bp_post = Blueprint('post', __name__, url_prefix='/post')

#create posts
@bp_post.route('/create_post', methods=['GET', 'POST'])
def create_post():
    return render_template('create_post.html')