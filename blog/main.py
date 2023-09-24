from flask import Blueprint, render_template

from .models.auth_register import User
from .models.posts import Posts
from sqlalchemy import func


bp_main = Blueprint('main', __name__)

# identify post user id


def get_user(id):
    post_user = User.query.get_or_404(id)
    return post_user

# random 2 posts on index


def best_posts1():
    posts_to_show1 = Posts.query.order_by(func.random()).limit(1).all()
    return posts_to_show1


def best_posts2():
    posts_to_show1 = Posts.query.order_by(func.random()).limit(1).all()
    return posts_to_show1


@bp_main.route('/', methods=['GET', 'POST'])
def index():
    post = Posts.query.all()
    return render_template('index.html', post=post,
                            get_user=get_user,
                            best_posts1=best_posts1,
                            best_posts2=best_posts2)


@bp_main.route('/article/<url>')
def show_article(url):
    post_view = Posts.query.filter_by(url=url).first()
    return render_template('article.html', post_view=post_view,
                            get_user=get_user)
