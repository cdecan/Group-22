from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# setting up SQLAlchemy and data models
# so we can map data models into database tables
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


class User(db.Model):
    """
    Contains info about the user data
    """
    # Basic user info
    id = db.Column(db.Integer, primary_key=True,
                   unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    billing_address = db.Column(db.String(120))
    postal_code = db.Column(db.String(120))
    balance = db.Column(db.Integer, nullable=True)

    def __repr__(self):
        return '<User %s>' % self.id
