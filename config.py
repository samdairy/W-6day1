import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config():
    """

    set config
    """
    SECRET_KEY = os.environ.get("SECRET_KEY") or "nana.nana.boo.boo.youll.never.guess"
    SQLALCHEMY_DATABASE_URI = os.environ.get("DEPLOY_DATABASE_URL") or "sqlite://" + os.path.join(basedir, 'app.db')
    SQLACHEMY_TRACK_MODIFICATION =False


