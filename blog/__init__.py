from flask import Flask, render_template, send_from_directory, session
from .models import db
from .models.auth_register import User


import os


def create_app(enviroment):
    
    app = Flask(__name__,)
    
    # config enviroment
    app.config.from_object(enviroment)
    
    #close session after 20 min
    @app.before_request
    def make_session_permanent():
        session.permanent = True
    
    
    
    @app.route('/')
    def index():
        user = True
        return render_template('index.html', user=user)
    
    
    # redirect node-flowbite files
    @app.route('/node_modules/<path:filename>')
    def serve_node_modules(filename):
        return send_from_directory(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'node_modules'), filename)
    
    #blueprint register
    from . import auth
    
    app.register_blueprint(auth.bp_auth)
    
    # db create
    with app.app_context():
        db.init_app(app)
        db.create_all()
    
    return app