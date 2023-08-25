from flask import Flask, render_template, send_from_directory
from .models import db
from .models.auth_register import User


import os


def create_app(enviroment):
    
    app = Flask(__name__,)
    
    app.config.from_object(enviroment)
    
    
    
    @app.route('/')
    def index():
        user = True
        return render_template('index.html', user=user)
    
    
    # redirect node-flowbite files
    @app.route('/node_modules/<path:filename>')
    def serve_node_modules(filename):
        return send_from_directory(os.path.join(os.path.abspath(os.path.dirname(__file__)), '..', 'node_modules'), filename)
    
    
    from . import auth
    
    app.register_blueprint(auth.bp_auth)
    
    with app.app_context():
        db.init_app(app)
        db.create_all()
    
    return app