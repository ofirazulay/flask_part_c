from flask import Blueprint, render_template

# TreatmentMenu blueprint definition
TreatmentMenu = Blueprint('TreatmentMenu', __name__, static_folder='static', static_url_path='/TreatmentMenu', template_folder='templates')


# Routes
@TreatmentMenu.route('/TreatmentMenu')
def index():
    return render_template('TreatmentMenu.html')
