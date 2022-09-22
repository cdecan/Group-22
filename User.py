from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# setting up SQLAlchemy and data models so we can map data models into database tables
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


class User(db.Model):
    """
    Contains info about the user data
    """
    # Basic user info
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    banking_info = db.Column(db.String(120), unique=True)
    balance = db.Column(db.Integer, primary_key=True)
    # Histories stored as PickleType
    transactions = db.Column(db.PickleType('Transaction'), mutable=True)
    listings = db.Column(db.PickleType('Listing'), mutable=True)
    reviews = db.Column(db.PickleType('Review'), mutable=True)

    def __repr__(self):
        return '<User %r>' % self.username
