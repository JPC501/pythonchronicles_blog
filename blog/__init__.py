from flask import Flask, session
from .models import db
from .models.auth_register import User
from .models.posts import Posts
from flask_ckeditor import CKEditor


def create_app(enviroment):

    app = Flask(__name__,)

    ckeditor = CKEditor(app)

    # config enviroment
    app.config.from_object(enviroment)

    # close session after 20 min
    @app.before_request
    def make_session_permanent():
        session.permanent = True

    # blueprint register
    from . import auth

    app.register_blueprint(auth.bp_auth)

    from . import posts

    app.register_blueprint(posts.bp_post)

    from .main import bp_main

    app.register_blueprint(bp_main)

    from .categories.categories_views import bp_categories

    app.register_blueprint(bp_categories)

    # db create
    with app.app_context():
        db.init_app(app)
        db.create_all()

    return app
