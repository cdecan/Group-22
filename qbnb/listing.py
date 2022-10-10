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
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    price = db.Column(db.Float, nullable=False)
    last_modified_date = db.Column(db.Date, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'),
                         nullable=False)
    owner = db.relationship('Listing', backref=db.backref('listings',
                                                          lazy=True))

    def __repr__(self):
        """A listing represents itself by displaying the associated title"""
        return '<Listing %r>' % self.title


def update_listing(listing_id, new_id, new_title, new_description, new_price):
    print()
