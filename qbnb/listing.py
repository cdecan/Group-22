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
    if not all(letter.isalnum() or letter.isspace() for letter in title)\
            or title.endswith(' ') or title.startswith(' '):
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


def update_listing(listing_id, new_id=None, new_title=None,
                   new_description=None, new_price=None):
    """Allows all attributes of a listing to be updated,
       excluding owner_id and last_modified_date.

    Args:
        listing_id (int, None): Unique id for the listing to change
        new_id (int, None): Updated id for the listing
        new_title (str, None): Updated title for the listing
        new_description (str, None): Updated description for the listing
        new_price (float, None): Updated price for the listing

    Returns:
        bool: Returns true if the listing was
              updated successfully and false otherwise.
    """

    # Get listing to update if it exists
    to_update = Listing.query.filter_by(id=listing_id).first()
    if not to_update:
        return False

    # Check that owner and their email exists
    owner = User.query.filter_by(id=to_update.owner_id).first()
    if not owner:
        return False
    if owner.email == '':
        return False

    # Ensures new id is not already taken
    if new_id is not None:
        is_id_taken = Listing.query.filter_by(id=new_id).all()
        if len(is_id_taken) > 0:
            return False
        to_update.id = new_id

    # Ensures new title follows the title requirements
    if new_title is not None:
        if new_title.endswith(' ') or new_title.startswith(' '):
            return False

        if not new_title.replace(' ', '').isalnum():
            return False

        if not (1 <= len(new_title) <= 80):
            return False

        is_title_taken = Listing.query.filter_by(title=new_title).all()
        if len(is_title_taken) > 0:
            return False

        to_update.title = new_title

    # Ensures new description follows the description requirements
    if new_description is not None:
        if (len(new_description) <= len(to_update.title)) or \
                (not (20 <= len(new_description) <= 2000)):
            return False

        to_update.description = new_description

    # Ensures new price follows the price requirements
    if new_price is not None:
        if (new_price <= to_update.price) or \
                (not (10 <= new_price <= 10000)):
            return False

        to_update.price = new_price

    # Updates the last modified date
    current_date = date.today()
    temp = current_date.strftime("%Y-%m-%d")
    temp = temp.replace('-', '')
    temp = int(temp)
    # Compares the current date with the required date range
    if not (20210102 < temp < 20250102):
        return False

    to_update.last_modified_date = current_date

    db.session.commit()
    return True
