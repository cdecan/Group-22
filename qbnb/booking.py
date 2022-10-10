from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# setting up SQLAlchemy and data models so
# we can map data models into database tables
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


class Booking(db.Model):
    """
    Contains information required to book a property.
    """

    # Booking ID
    id = db.Column(db.Integer, unique=True, primary_key=True)
    # ID of the user making the booking.
    user_id = db.Column(db.Integer, unique=True, nullable=False)
    # ID of the listing to be booked.
    listing_id = db.Column(db.Integer, unique=True, nullable=False)
    # Listing price
    price = db.Column(db.Float,
                      db.ForeignKey('Listing.price'), nullable=False)
    # Booking date.
    date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        """Each booking will be represented by a unique ID"""
        return '<Booking %r>' % self.id
