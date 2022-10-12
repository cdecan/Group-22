from flask_sqlalchemy import SQLAlchemy
from qbnb import app

# setting up SQLAlchemy and data models
# so we can map data models into database tables
db = SQLAlchemy(app)


class User(db.Model):
    """
    Contains info about the user data
    """
    # Auto generated user id that is unique
    id = db.Column(db.Integer, primary_key=True,
                   unique=True, nullable=False)
    # user email, cannot be null
    email = db.Column(db.String(120), unique=True, nullable=False)
    # password of user, cannot be null
    password = db.Column(db.String(120), nullable=False)
    # username of user, cannot be null
    username = db.Column(db.String(80), unique=True, nullable=False)
    # billing_address, null only for sprint 2
    billing_address = db.Column(db.String(120))
    # postal code of user, null only for sprint 2
    postal_code = db.Column(db.String(120))
    # balance of user, cannot be null
    balance = db.Column(db.Integer)

    def __repr__(self):
        return '<User %s>' % self.id


db.create_all()
