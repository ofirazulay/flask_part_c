from flask import Blueprint, render_template

# calander blueprint definition
calander = Blueprint('calander', __name__, static_folder='static', static_url_path='/calander', template_folder='templates')


# Routes
@calander.route('/calander')
def index():
    return render_template('calander.html')
