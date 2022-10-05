from flask import Flask
from qbnb import app
from flask_sqlalchemy import SQLAlchemy


# setting up SQLAlchemy and data models
# so we can map data models into database tables
db = SQLAlchemy(app)


class User(db.Model):
    """
    Contains info about the user data
    """
    # Basic user info
    user_id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    banking_info = db.Column(db.String(120), unique=True, nullable=True)
    balance = db.Column(db.Integer, nullable=True)
    # Histories stored as PickleType
    # possible removal in the next sprint
    transactions = db.Column(db.PickleType(mutable=True), nullable=True)
    listings = db.Column(db.PickleType(mutable=True), nullable=True)
    reviews = db.Column(db.PickleType(mutable=True), nullable=True)

    def __repr__(self):
        return '<User %s>' % self.user_id


db.create_all()
