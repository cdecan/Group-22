from flask_sqlalchemy import SQLAlchemy
from qbnb import app
import re

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


def update_email(user_id: int, new_email: str):
    """
    Updates the email associated with this user
    Parameters:
        user_id (int): ID of user to update
        new_email (string): new user email
    Returns:
        True if email update succeeded otherwise False
    """
    # Find user to update
    u = User.query.filter_by(id=user_id).first()
    if u is None:
        return False
    # Update value and save to database
    u.email = new_email
    db.session.commit()
    # Success
    return True


def update_username(user_id: int, new_username: str):
    """
    Updates the username associated with this user
    Parameters:
        user_id (int): ID of user to update
        new_username (string): new userame
    Returns:
        True if username update succeeded otherwise False
    """
    # Find user to update
    u = User.query.filter_by(id=user_id).first()
    if u is None:
        return False
    # Ensure username between 2-19 characters
    if (len(new_username) < 2 or len(new_username) >= 20):
        return False
    # Ensure only alphanumeric characters
    if (not new_username.isalnum()):
        return False
    # Ensure no space as prefix/suffix
    if (new_username.startswith(' ') or new_username.endswith(' ')):
        return False
    # Update value and save to database
    u.username = new_username
    db.session.commit()
    # Success
    return True


def update_billing_address(user_id: int, new_billing_address: str):
    """
    Updates the billing address associated with this user
    Parameters:
        user_id (int): ID of user to update
        new_billing_address (string): new billing address
    Returns:
        True if billing address update succeeded otherwise False
    """
    # Find user to update
    u = User.query.filter_by(id=user_id).first()
    if u is None:
        return False
    # Update value and save to database
    u.billing_address = new_billing_address
    db.session.commit()
    # Success
    return True


def update_postal_code(user_id: int, new_postal_code: str):
    """
    Updates the postal code associated with this user
    Parameters:
        user_id (int): ID of user to update
        new_postal_code (string): new postal code (eg. "A1A 1A1")
    Returns:
        True if postal code update succeeded otherwise False
    """
    # Find user to update
    u = User.query.filter_by(id=user_id).first()
    if u is None:
        return False
    # Ensure valid postal code
    pattern = re.compile("^([A-Z][0-9][A-Z] [0-9][A-Z][0-9])$", re.IGNORECASE)
    if len(pattern.match(new_postal_code)) == 0:
        return False
    # Update value and save to database
    u.postal_code = new_postal_code
    db.session.commit()
    # Success
    return True


db.create_all()
