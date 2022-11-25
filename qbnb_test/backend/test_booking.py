from flask_sqlalchemy import SQLAlchemy
from qbnb.listing import Listing
from qbnb.user import User
from qbnb.booking import book_listing
import datetime
from qbnb import app

db = SQLAlchemy(app)

user1 = User(id=1,
             email="user1@test.com",
             password="Password1_",
             username="User1",
             billing_address="",
             postal_code="",
             balance=1000)
user2 = User(id=2,
             email="user2@test.com",
             password="Password2_",
             username="User2",
             billing_address="",
             postal_code="",
             balance=1000)

test_date1 = datetime.datetime(2021, 8, 5)
test_date2 = datetime.datetime(2021, 8, 6)
test_listing_1 = Listing(id=1,
                         title="listing 1",
                         description="This is a description of Listing 1",
                         price=10.00,
                         last_modified_date=test_date1,
                         owner_id=1)
test_listing_2 = Listing(id=2,
                         title="listing 2",
                         description="This is a description of Listing 2",
                         price=5000.00,
                         last_modified_date=test_date2,
                         owner_id=1)
test_listing_3 = Listing(id=3,
                         title="listing 3",
                         description="This is a description of Listing 3",
                         price=10.00,
                         last_modified_date=test_date1,
                         owner_id=1)
db.session.add(user1)
db.session.add(user2)
db.session.add(test_listing_1)
db.session.add(test_listing_2)
db.session.add(test_listing_3)
db.session.commit()


def test_r1():
    """
        Testing R1: A user can book a listing.
    """

    assert book_listing(2, 1) is True


def test_r2():
    """
        Testing R2: A user cannot book a listing for his/her listing.
    """

    assert book_listing(1, 1) is False


def test_r3():
    """
        Testing R3: A user cannot book a listing that costs more than his/her balance.
    """

    assert book_listing(2, 2) is False


def test_r4():
    """
        Testing R4: A user cannot book a listing that is already booked with the overlapped dates.
    """

    assert book_listing(2, 3) is False


def test_r6():
    """
        Testing R6: User id exists in the database
    """
    assert book_listing(3, 3) is False


def test_r7():
    """
        Testing R7: Listing id exists in the database
    """
    assert book_listing(2, 4) is False


def test_r8():
    """
        Testing R8: Price has to be of range [10, 10000].
    """
    pass


def test_r9():
    """
        Testing R9: Date must be after 2021-01-02 and before 2025-01-02
    """
    pass


def test_r10():
    """
        Testing R10: User balance is correctly updated upon successful booking
    """
    pass
