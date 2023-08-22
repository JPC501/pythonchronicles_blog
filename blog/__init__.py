from flask import Flask, render_template, send_from_directory

import os


def create_app():
    
    app = Flask(__name__,)
    
    
    
    
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
    
    return app