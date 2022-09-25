from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# setting up SQLAlchemy and data models so
# we can map data models into database tables
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


class Transaction(db.Model):
    """
    Contains information required to complete a transaction
    between two users.
    """
    # Transaction ID
    id = db.Column(db.Integer, unique=True, primary_key=True)
    # ID of the user renting the property.
    id_renter = db.Column(db.Integer, unique=True, nullable=False)
    # ID of the user listing their property to be rented.
    id_owner = db.Column(db.Integer, unique=True, nullable=False)
    # Listing price dollars
    listing_price_dollars = db.Column(
        db.Integer, db.ForeignKey('Listing.price_dollars'), nullable=False)
    # Listing price cents
    listing_price_cents = db.Column(
        db.Integer, db.ForeignKey('Listing.price_cents'), nullable=False)
    # listing availability.
    listing_availability = db.Column(
        db.Boolean, db.ForeignKey('Listing.availability'), nullable=False)
    # Relationship to listing entity.
    listing = db.relationship('Listing', backref='listing', lazy=True)

    def __repr__(self):
        """Each listing will be represented by a unique ID"""
        return '<Transaction %r>' % self.id
