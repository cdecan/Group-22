from flask import Flask
from qbnb import app
from flask_sqlalchemy import SQLAlchemy


# Setting up SQLAlchemy and data models so we can map data models into
# database tables
db = SQLAlchemy(app)


class Review(db.Model):
    """
    Contains information about a listing review.
    """
    # Unique ID for this review
    id = db.Column(db.Integer, primary_key=True)
    # Unique ID for user who authored review
    author_id = db.Column(db.Integer, unique=True, nullable=False)
    # Unique ID for listing this review is of
    listing_id = db.Column(db.Integer, unique=True, nullable=False)
    # Rating out of 5
    rating = db.Column(db.Integer, unique=True, nullable=False)
    # Review date
    review_date = db.Column(db.Date, unique=True, nullable=False)
    # Review body (max 1000 chars)
    review_body = db.Column(db.String(1000), unique=True, nullable=False)

    def __repr__(self):
        return f'Review {self.id}'


