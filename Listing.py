from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# setting up SQLAlchemy and data models so we can map data models into database tables
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


class Listing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    creator = db.relationship('User', backref='listing', uselist=False, lazy=True)
    address = db.Column(db.String(120), unique=True, nullable=False)
    price = db.Column(db.Integer, primary_key=True, nullable=False)
    number_of_guests = db.Column(db.Integer, primary_key=True, nullable=False)
    number_of_beds = db.Column(db.Integer, primary_key=True, nullable=False)
    number_of_bathrooms = db.Column(db.Integer, primary_key=True, nullable=False)
    list_date = db.Column(db.Date, primary_key=True, nullable=False)
    availability = db.Column(db.Boolean, primary_key=True, nullable=False)
    reviews = db.relationship('Review', backref='listing', lazy=True)

    def __repr__(self):
        return '<Listing %r>' % self.address
