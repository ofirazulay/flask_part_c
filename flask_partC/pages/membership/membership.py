from flask import Blueprint, render_template

# membership blueprint definition
membership = Blueprint('membership', __name__, static_folder='static', static_url_path='/membership', template_folder='templates')


# Routes
@membership.route('/membership')
def index():
    return render_template('membership.html')
