from flask import Blueprint, render_template

bp_auth = Blueprint('auth', __name__, url_prefix='/auth')

@bp_auth.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('auth_templates/login.html')