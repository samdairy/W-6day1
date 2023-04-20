from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import uuid
from datetime import datetime

#adding flask security for passwords
from werkzeug.security import generate_password_hash, check_password_hash

#import secrets module(from python) generates a token for each user
import secrets

db = SQLAlchemy()

class User(db.Model):
    id = db.Column(db.String, primary_key = True)
    first_name =db.Column(db,String(150), nullable = True, default = '')
    last_name = db.Column(db.String(150), nullable = True, default = '')
    email = db.Column(db.String(150), nullable = False)
    password = db.Column(db.String(150),nullable = True, default = '')
    username = db.Column(db.Sting(150), nullable = False)
    token = db.Column(db.String,default = '', unique = True)
    date_created = db.Column(db.DateTime, nullable = False,defaulte = datetime.utcnow)



    def __init__(self, email, username, first_name = '', last_name = '', password = ''):
        self.id = self.set_id()
        self.first_name = first_name
        self.last_name = last_name
        self.password = self.set_password(password)
        self.email = email
        self.username = username
        self.token = self.set_token(24)


    def set_token(self, length):
        return secrets.token_hex(length)
    
    def set_id(self):
        return str(uuid.uuid4())
    
    def set_password(self, password)
        self.pw_hash = generate_password_hash(password)
        return self.pw_hash
    
    def __repr__(self):
        return f"User {self.email} has ben adde to the database!"

        