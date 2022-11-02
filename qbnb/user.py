from flask_sqlalchemy import SQLAlchemy
import re
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
# db.drop_all()
# create table
db.create_all()


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
    if (len(new_username) <= 2 or len(new_username) >= 20):
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
    pattern = re.compile("([A-Z][0-9][A-Z] [0-9][A-Z][0-9])", re.IGNORECASE)
    if pattern.match(new_postal_code) is None:
        return False
    # Update value and save to database
    u.postal_code = new_postal_code
    db.session.commit()
    # Success
    return True


def register(name, email, password):
    """
    Register a new user, template is copied from models.py
      Parameters:
        name (string):     user name
        email (string):    user email
        password (string): user password
      Returns:
        0 if registration succeeded otherwise an integer
        representing the error given
    """
    # validating
    if check_email(email) is False:
        return 1
    if check_name(name) is False:
        return 2
    if check_password(password) is False:
        return 3

    # check if the email has been used:
    existed = User.query.filter_by(email=email).all()
    if len(existed) > 0:
        return 4

    # create a new user
    user = User(username=name, email=email, password=password,
                billing_address="", postal_code="", balance=100)

    # add it to the current database session
    db.session.add(user)

    # actually save the user object
    db.session.commit()

    return 0


def check_email(email):
    """
    Check validity of the given email address.

    Parameters:
        email (str): Email address

    Returns:
        bool: True if valid, False otherwise
    """
    # check if email or password is empty
    if len(email) == 0:
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
    return True


def check_name(name):
    """
    Check validity of the given username.

    Parameters:
        name (str): User name

    Returns:
        bool: True if valid, False otherwise
    """
    # validating the username
    if len(name) <= 2 or len(name) >= 20 or name[0] == " " or name[-1] == " ":
        return False
    # to validate that the name without spaces is all alphanumeric
    temp_name = name.replace(" ", "")
    if not temp_name.isalnum():
        return False
    return True


def check_password(password):
    """
    Check validity of the given password.

    Parameters:
        password (str): Password

    Returns:
        bool: True if valid, False otherwise
    """
    if len(password) == 0:
        return False
    # validating the password using regex
    regex_password = re.compile("^(?=.*[a-z])(?=." +
                                "*[A-Z])(?=.*\\d)" +
                                "(?=.*[-+_!@#$%^&*., ?]).+$")
    if not (len(password) > 6 and re.search(regex_password, password)):
        return False
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
    # validating
    if check_email(email) is False:
        return None
    if check_password(password) is False:
        return None

    valid = User.query.filter_by(email=email, password=password).all()
    if len(valid) != 1:
        return None
    return valid[0]
