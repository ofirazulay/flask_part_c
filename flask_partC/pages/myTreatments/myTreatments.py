from flask import Blueprint, render_template

# myTreatments blueprint definition
myTreatments = Blueprint('myTreatments', __name__, static_folder='static', static_url_path='/myTreatments', template_folder='templates')


# Routes
@myTreatments.route('/myTreatments')
def index():
    return render_template('myTreatments.html')
