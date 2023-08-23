from flask import Blueprint, render_template

bp_auth = Blueprint('auth', __name__, url_prefix='/auth')

#login form
@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('auth/login.html')

#register form
@bp_auth.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('auth/register.html')