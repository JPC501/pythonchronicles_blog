from flask import(
    Blueprint, render_template,
    redirect, g, flash, url_for
    
)

bp_categories = Blueprint('categories', __name__, url_prefix='/categories')


#  show routes of categories

@bp_categories.route('/Backend', methods=['GET', 'POST'])
def backend():
    return render_template('categories/backend.html')
