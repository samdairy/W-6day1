from flask import Flask
from config import Config 
from.site.routes import site
from.authentication.routes import auth
from.model import db as root_db

from flask_migrat import Migrate

#flask CORS imort - CROSS ORIGIN RESOURCE SHARING -future proofing
#our react app so it can make api calls to this flask app
from flask_cors import CORS
app = Flask(__name__)

app.register_blueprint(site)
app.register_blueprint(auth)
app.config.from_object(Config)

root_db.init_app(app)

migrate = Migrate(app, root_db)


CORS(app)


