from flask_sqlalchemy import SQLAlchemy
from qbnb import app
from qbnb.user import User
from qbnb.listing import Listing
import datetime

# setting up SQLAlchemy and data models so
# we can map data models into database tables
db = SQLAlchemy(app)


class Booking(db.Model):
    """
    Contains information required to book a property.
    """

    # Booking ID
    id = db.Column(db.Integer, unique=True, primary_key=True)
    # ID of the user making the booking.
    user_id = db.Column(db.Integer, unique=True, nullable=False)
    # ID of the listing to be booked.
    listing_id = db.Column(db.Integer, unique=True, nullable=False)
    # Listing price
    price = db.Column(db.Float,
                      db.ForeignKey(Listing.price), nullable=False)
    # Booking date.
    date = db.Column(db.DateTime, nullable=False)

    def __repr__(self):
        """Each booking will be represented by a unique ID"""
        return '<Booking %r>' % self.id


db.create_all()


def book_listing(booker_id, listing_id):
    """
    A function to create a booking for a user with id booker_id
    who wants to book listing with listing_id

    Args:
        booker_id (int): ID of the user making the booking
        listing_id (int): ID of the listing being booked

    Returns:
        bool: Returns true if the booking was
              created successfully and false otherwise.
    """

    # Check if the owner id exists
    user = User.query.get(booker_id)
    if user is None:
        return False

    # Check if the listing id exists
    listing = Listing.query.get(listing_id)
    if listing is None:
        return False

    # The price of the booking is the price of the listing
    my_price = listing.price

    # Check that price is a float just in case
    if not isinstance(my_price, (float, int)):
        return False

    # The booking was created today
    creation_date = datetime.datetime.now()

    # A user cannot book a listing for his/her listing.
    if listing.owner_id == booker_id:
        return False

    # A user cannot book a listing that costs more than his/her balance.
    if my_price > user.balance:
        return False

    # A user cannot book a listing that is already
    # Booked with the overlapped dates.
    bookings_with_same_listing = \
        Booking.query.filter_by(listing_id=listing_id).all()

    for my_booking in bookings_with_same_listing:
        if my_booking.date.date() == datetime.date.today():
            return False

    booking = Booking(user_id=booker_id,
                      listing_id=listing_id,
                      price=my_price,
                      date=creation_date)

    # User pays for the listing
    user.balance -= my_price

    db.session.add(booking)
    db.session.commit()
    return True
