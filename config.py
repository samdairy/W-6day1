import os
from dotenv import load_dotenv

basedir = os.path.abspath(os.path.dirname(__file__))



load_dotenv(os.path.join(basedir, '.env'))


class Config():
    """

    set config variables for the flask app.
    Using Envirment Variables wher availble otherwise
    create the config variable if not done already

    """

    FLASK_APP = os.environ.get('FLASK_APP')
    FLASK_ENV = os.environ.get('FLASK_ENV')
    SECRET_KEY = os.environ.get("SECRET_KEY") or "nana.nana.boo.boo.youll.never.guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEPLOY_DATABASE_URL") or "sqlite://" + os.path.join(basedir, 'app.db')
    SQLACHEMY_TRACK_MODIFICATION =False


