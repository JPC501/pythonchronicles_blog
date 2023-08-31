from flask import Blueprint, render_template, url_for, g, redirect
from .auth import login_required


pf = Blueprint('user', __name__, url_prefix='/user')

# show profile
@pf.route('/profile', methods=['GET'])
@login_required
def profile():
    return render_template('authentication/profile.html')

# edit profile

@pf.route('/edit_profile', methods=['GET', 'POST'])
@login_required
def edit_profile():
    return render_template('authentication/edit_profile.html')