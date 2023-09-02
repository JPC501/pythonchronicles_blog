from flask import Blueprint, render_template, request, redirect, url_for, flash, session, g 
from .models.auth_register import User
from werkzeug.security import generate_password_hash, check_password_hash

from . import db

bp_auth = Blueprint('auth', __name__, url_prefix='/auth')


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
        email_validator = User.query.filter_by(email=email).first()
        
        if not user_name_validator and not email_validator:
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))
        else:
            if user_name_validator != None:
                error = f'El nombre de suario ya existe, elija otro!'
                flash(error)
            elif email_validator != None:
                error = f'El Email ya existe, elija otro!'
                flash(error)
    
    return render_template('authentication/register.html')

#login form
@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    
    if request.method == 'POST':
        email = request.form.get('email')
        password = request.form.get('password')
        
        user = User.query.filter_by(email=email).first()
        
        if user is None:
            error = 'usuario no encontrado'
        elif not check_password_hash(user.password, password):
            error = 'contraseña incorrecta'
            
        if error == None:
            session.clear()
            session['user.id'] = user.id
            
            return redirect(url_for('index'))
        
    return render_template('authentication/login.html', error=error)

#keep user logged

@bp_auth.before_app_request
def load_user():
    user_id = session.get('user.id')

    if user_id == None:
        g.user = None
    else:
        g.user = User.query.get_or_404(user_id)
        
#profile

import functools
#protecting the views

def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            return redirect(url_for('auth.login'))
        return view(**kwargs)
    return wrapped_view

#show profile 
@bp_auth.route('/profile', methods=['GET'])
@login_required
def profile():
    user = User.query.get_or_404(g.user.id)
    return render_template('authentication/profile.html', user=user)


#edit profile 
@bp_auth.route('/edit_profile/<int:id>', methods=['GET', 'POST'])
@login_required
def edit_profile(id):
    user = User.query.get_or_404(id)
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        password = request.form.get('password')
        
        
        error = None
        
        if password is not None:
            if len(password) < 6:
                error = 'La contraseña debe tener más de 6 caracteres.'
        else:
            user.password = generate_password_hash(password)
            
        if name is not None and name != "":
            user.name = name
        if email is not None and email != "":
            user.email = email
            
        
        if error is not None:
            flash(error)
        else:
            db.session.commit()
            return redirect(url_for('auth.profile'))
        
    return render_template('authentication/edit_profile.html')
        
# close session

@bp_auth.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))




#! pendiente eliminar esto y ponerlo en posts
@bp_auth.route('/create_post', methods=['GET', 'POST'])
def create_post():
    return render_template('create_post.html')