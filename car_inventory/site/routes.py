from flask import blueprint,render_template


site = Blueprint('site', __name__, template_folder='site_templates' )



@site.route('/')
def home():
    
    return "Hello World again, hey this is cool look at my application, Mom!"
