from flask import Blueprint, render_template
from utilities.db.db_manager import dbManager


# ContactUs blueprint definition
ContactUs = Blueprint('ContactUs', __name__, static_folder='static', static_url_path='/ContactUs', template_folder='templates')


# Routes
@ContactUs.route('/ContactUs')
def index():
    return render_template('ContactUs.html')
