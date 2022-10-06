# from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from qbnb.user import User
from datetime import date
from qbnb import app

# setting up SQLAlchemy and data models
# so we can map data models into database tables
db = SQLAlchemy(app)


class Listing(db.Model):
    """
    Contains information about the property listings
    """
    # each listing has a unique id
    id = db.Column(db.Integer, unique=True, primary_key=True)
    # each listing has a unique title
    title = db.Column(db.String, unique=True, nullable=False)
    # each listing has a description
    description = db.Column(db.String, nullable=True)
    # each listing has a price
    price = db.Column(db.Float, nullable=False)
    # each listing has a last modified date
    last_modified_date = db.Column(db.Date, nullable=True)
    # each listing has an owner with a unique id
    owner_id = db.Column(db.Integer, db.ForeignKey(User.id),
                         nullable=True)

    def __repr__(self):
        """A listing represents itself by displaying the associated title"""
        return '<Listing %r>' % self.title


db.create_all()


def create_listing(owner_id, title, description, price):
    # get the user posting the listing
    user = User.query.get(owner_id)
    if not user:
        return False
    # check if user email exists
    email_existed = User.query.filter_by(email=user.email).all()
    if not len(email_existed) > 0:
        return False
    if user.email == "":
        return False
    # check if title meets criteria:
    if len(title) < 1 or len(title) > 80:
        return False
    if not title.isalnum() or title.endswith(' ') or title.startswith(' '):
        return False
    title_existed = Listing.query.filter_by(title=title).all()
    if len(title_existed) > 0:
        return False
    # check if description meets criteria:
    if len(description) < 20 or len(description) > 2000 \
            or len(description) < len(title):
        return False
    # check if price meets criteria:
    if price < 10 or price > 10000:
        return False
    # product was just created
    last_modified_date = date.today()

    # listing is ok -> make listing
    listing = Listing(title=title, description=description, price=price,
                      last_modified_date=last_modified_date, owner_id=owner_id)
    db.session.add(listing)
    db.session.commit()
    return True
