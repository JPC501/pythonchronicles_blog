from flask import Blueprint, render_template, request, redirect, url_for, flash
from .models.auth_register import User
from werkzeug.security import generate_password_hash, check_password_hash

from . import db

bp_auth = Blueprint('auth', __name__, url_prefix='/auth')

#login form
@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html')



#register form
@bp_auth.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User(name, email, generate_password_hash(password))
        
        error = None
        user_name_validator = User.query.filter_by(name=name).first()
        
        if user_name_validator == None:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            error = f'el usuario{name} ya existe, elija otro'
            flash(error)
    
    return render_template('auth/register.html')



#prifile users
@bp_auth.route('/profile', methods=['GET', 'POST'])
def profile():
    return render_template('auth/profile.html')
