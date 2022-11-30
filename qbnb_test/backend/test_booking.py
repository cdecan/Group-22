from flask_sqlalchemy import SQLAlchemy
from qbnb.listing import Listing
from qbnb.listing import create_listing
from qbnb.user import User
from qbnb.user import register
from qbnb.booking import Booking
from qbnb.booking import book_listing
import datetime
from qbnb import app

db = SQLAlchemy(app)

for i in range(5):
    register(f"User{i + 1}", f"user{i + 1}@gmail.com", f"Password{i + 1}_")

create_listing(1,
               "listing 1",
               "This is a description of listing 1",
               10.00)
create_listing(1,
               "listing 2",
               "This is a description of listing 2",
               10.00)
create_listing(1,
               "listing 3",
               "This is a description of listing 3",
               5000.00)
create_listing(1,
               "listing 4",
               "This is a description of listing 4",
               10.00)
test_date1 = datetime.datetime(2021, 8, 5)
test_listing_5 = Listing(id=5,
                         title="listing 5",
                         description="This is a description of Listing 5",
                         price=20000.00,
                         last_modified_date=test_date1,
                         owner_id=1)
test_listing_6 = Listing(id=6,
                         title="listing 6",
                         description="This is a description of Listing 6",
                         price=2.00,
                         last_modified_date=test_date1,
                         owner_id=1)
db.session.add(test_listing_5)
db.session.add(test_listing_6)
db.session.commit()
create_listing(1,
               "listing 7",
               "This is a description of listing 7",
               10.00)
create_listing(1,
               "listing 8",
               "This is a description of listing 8",
               10.00)


def test_r1():
    """
        Testing R1: A user can book a listing.
    """
    assert book_listing(2, 1) is True


def test_r2():
    """
        Testing R2: A user cannot book a listing for his/her listing.
    """
    assert book_listing(1, 2) is False


def test_r3():
    """
        Testing R3: A user cannot book a listing
        that costs more than his/her balance.
    """
    assert book_listing(3, 3) is False


def test_r4():
    """
        Testing R4: A user cannot book a listing that
        is already booked with the overlapped dates.
    """
    assert book_listing(3, 1) is False


def test_r6():
    """
        Testing R6: User id exists in the database
    """
    assert book_listing(6, 4) is False


def test_r7():
    """
        Testing R7: Listing id exists in the database
    """
    assert book_listing(4, 10) is False


def test_r8():
    """
        Testing R8: Price has to be of range [10, 10000].
    """
    assert book_listing(4, 5) is False
    assert book_listing(4, 6) is False


def test_r9():
    """
        Testing R9: Date must be after 2021-01-02 and before 2025-01-02
    """
    assert book_listing(4, 7) is True
    temp = Booking.query.filter_by(id=2).first()
    temp = temp.date
    lower_bound = datetime.datetime(2021, 1, 2, 23, 59, 59)
    upper_bound = datetime.datetime(2025, 1, 2)
    assert lower_bound < temp < upper_bound


def test_r10():
    """
        Testing R10: User balance is correctly updated upon successful booking
    """
    temp = User.query.filter_by(id=5).first()
    balance_before = temp.balance

    assert book_listing(5, 8) is True

    temp = User.query.filter_by(id=5).first()
    balance_after = temp.balance

    assert balance_after < balance_before
