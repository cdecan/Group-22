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
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(120), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    billing_address = db.Column(db.String(120), nullable=False)
    postal_code = db.Column(db.String(120), nullable=False)
    balance = db.Column(db.Integer, nullable=False)

    # possible removal in the next sprint

    # bookings = db.relationship('Booking',backref='bookings',lazy=True)
    # listings = db.relationship('Listing', backref='listings', lazy=True)
    # reviews = db.relationship('Review', backre='reviews', lazy=True)f

    def __repr__(self):
        return '<User %s>' % self.id
