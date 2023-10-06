from flask import (
    Blueprint, render_template

)

bp_categories = Blueprint('categories', __name__, url_prefix='/categories')


#  show routes of categories

@bp_categories.route('/backend', methods=['GET', 'POST'])
def backend():
    return render_template('categories/backend.html')


@bp_categories.route('data', methods=['GET', 'POST'])
def data_analysis():
    return render_template('categories/data.html')


@bp_categories.route('gaming', methods=['GET', 'POST'])
def gaming():
    return render_template('categories/gaming.html')
