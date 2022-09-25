# tested with flake8
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# setting up SQLAlchemy and data models
# so we can map data models into database tables
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


class Listing(db.Model):
    """
    Contains information about the property listings
    """
    id = db.Column(db.Integer, primary_key=True)
    # A review is posted by a user.
    creator = db.relationship('User', backref='listing',
                              uselist=False, lazy=True)
    # basic info about the property to be shown to the user
    address = db.Column(db.String(120), unique=True, nullable=False)
    price = db.Column(db.Float, nullable=False)
    number_of_guests = db.Column(db.Integer, nullable=False)
    number_of_beds = db.Column(db.Integer, nullable=False)
    number_of_bathrooms = db.Column(db.Integer, nullable=False)
    list_date = db.Column(db.Date, nullable=False)
    availability = db.Column(db.Boolean, nullable=False)
    # a listing can contain many reviews
    reviews = db.relationship('Review', backref='listing', lazy=True)

    def __repr__(self):
        """A listing represents itself by displaying the associated address"""
        return '<Listing %r>' % self.address
