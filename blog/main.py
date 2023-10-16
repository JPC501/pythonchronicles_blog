from flask import Blueprint, render_template
from .models.auth_register import User
from .models.posts import Posts
from sqlalchemy import func

# Define a Blueprint for 'main' related routes
bp_main = Blueprint('main', __name__)


def get_user(id):
    """
    Fetch a user by their ID.

    Parameters:
    - id (int): ID of the user

    Returns:
    - User object
    """
    post_user = User.query.get_or_404(id)
    return post_user


def best_posts1():
    """
    Randomly select 1 post from the database.

    Returns:
    - List containing 1 Posts object
    """
    posts_to_show1 = Posts.query.order_by(func.random()).limit(1).all()
    return posts_to_show1


def best_posts2():
    """
    Randomly select 1 post from the database.

    Returns:
    - List containing 1 Posts object
    """
    posts_to_show1 = Posts.query.order_by(func.random()).limit(1).all()
    return posts_to_show1


@bp_main.route('/', methods=['GET', 'POST'])
def index():
    """
    Render the home page.

    Template:
    - index.html

    Allowed Methods:
    - GET: To render the page.
    - POST: Although included, no specific action is taken.
    """
    post = Posts.query.all()
    return render_template('index.html', post=post,
                            get_user=get_user,
                            best_posts1=best_posts1,
                            best_posts2=best_posts2)


@bp_main.route('/article/<url>')
def show_article(url):
    """
    Render an individual article page.

    Parameters:
    - url (str): URL of the article

    Template:
    - article.html
    """
    post_view = Posts.query.filter_by(url=url).first()
    return render_template('article.html', post_view=post_view,
                            get_user=get_user)
