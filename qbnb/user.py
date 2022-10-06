from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import re

# setting up SQLAlchemy and data models
# so we can map data models into database tables
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
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
    username = db.Column(db.String(80), unique=False, nullable=False)
    # billing_address, cannot be null but can be ""
    billing_address = db.Column(db.String(120), nullable=False)
    # postal code of user, cannot be null but can be ""
    postal_code = db.Column(db.String(120), nullable=False)
    # balance of user, cannot be null but can be 0
    balance = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return '<User %s>' % self.id


# to fix the bug with app.app_context
app.app_context().push()
# drop previous table if exists
# makes sure that no previous data remaining to mess with testing
# will be removed later when actual data is needed
db.drop_all()
# create table
db.create_all()


def register(name, email, password):
    """
    Register a new user, template is copied from models.py
      Parameters:
        name (string):     user name
        email (string):    user email
        password (string): user password
      Returns:
        True if registration succeeded otherwise False
    """
    # check if email or password is empty
    if len(email) == 0 or len(password) == 0:
        return False

    # validating the email using regex,
    # RFC 5322 is too hard to validate because of the use of "" in address,
    # so this is a more universal validation
    regex_email = re.compile(r"^[a-z0-9!#$%&'*+/=?^_`{|}~-]+"
                             r"(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)"
                             r"*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)"
                             r"+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?$")
    if not re.fullmatch(regex_email, email):
        return False

    # validating the password using regex
    regex_password = re.compile("^(?=.*[a-z])(?=." +
                                "*[A-Z])(?=.*\\d)" +
                                "(?=.*[-+_!@#$%^&*., ?]).+$")
    if not (len(password) > 6 and re.search(regex_password, password)):
        return False

    # validating the username
    if len(name) < 2 or len(name) > 20 or name[0] == " " or name[-1] == " ":
        return False
    # to validate that the name without spaces is all alphanumeric
    temp_name = name.replace(" ", "")
    if not temp_name.isalnum():
        return False

    # check if the email has been used:
    existed = User.query.filter_by(email=email).all()
    if len(existed) > 0:
        return False

    # create a new user
    user = User(username=name, email=email, password=password,
                billing_address="", postal_code="", balance=100)

    # add it to the current database session
    db.session.add(user)

    # actually save the user object
    db.session.commit()

    return True


def login(email, password):
    """
    Check login information, this is copied from models.py
      Parameters:
        email (string):    user email
        password (string): user password
      Returns:
        The user object if login succeeded otherwise None
    """
    valid = User.query.filter_by(email=email, password=password).all()
    if len(valid) != 1:
        return None
    return valid[0]
