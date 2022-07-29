from flask import Blueprint, render_template

# paymentPage blueprint definition
paymentPage = Blueprint('paymentPage', __name__, static_folder='static', static_url_path='/paymentPage', template_folder='templates')


# Routes
@paymentPage.route('/paymentPage')
def index():
    return render_template('paymentPage.html')
