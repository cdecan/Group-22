from flask_sqlalchemy import SQLAlchemy
import datetime
from qbnb import app
from qbnb.listing import Listing
from qbnb.listing import update_listing
from qbnb.user import User

db = SQLAlchemy(app)

user1 = User(id=1,
             email="test@test.com",
             password="Password_",
             username="User1",
             billing_address="",
             postal_code="",
             balance=100)
user2 = User(id=2,
             email="",
             password="Password_",
             username="User2",
             billing_address="",
             postal_code="",
             balance=100)

test_date = datetime.datetime(2021, 8, 5).strftime("%Y-%m-%d")
test_listing_1 = Listing(id=1,
                         title="listing 1",
                         description="description",
                         price=20.00,
                         last_modififed_date=test_date,
                         owner_id=1)
test_listing_2 = Listing(id=2,
                         title="listing 2",
                         description="description",
                         price=20.00,
                         last_modififed_date=test_date,
                         owner_id=1)
test_listing_3 = Listing(id=3,
                         title="listing 3",
                         description="description",
                         price=20.00,
                         last_modififed_date=test_date,
                         owner_id=1)
test_listing_4 = Listing(id=4,
                         title="listing 4",
                         description="description",
                         price=20.00,
                         last_modififed_date=test_date,
                         owner_id=1)
test_listing_5 = Listing(id=5,
                         title="listing 5",
                         description="description",
                         price=20.00,
                         last_modififed_date=test_date,
                         owner_id=2)
test_listing_6 = Listing(id=6,
                         title="listing 6",
                         description="description",
                         price=20.00,
                         last_modififed_date=test_date,
                         owner_id=3)
db.session.add(user1)
db.session.add(user2)
db.session.add(test_listing_1)
db.session.add(test_listing_2)
db.session.add(test_listing_3)
db.session.add(test_listing_4)
db.session.add(test_listing_5)
db.session.add(test_listing_6)
db.session.commit()


def test_r5_1_update_listing():
    """
    Testing R5-1: Can one update all attributes of the
    listing, except owner_id and last_modified_date.
    """

    assert update_listing(1,
                          7,
                          None,
                          "this is a correct description",
                          21.00) is True
    assert update_listing(7,
                          1,
                          None,
                          "this is a correct description",
                          None) is True
    assert update_listing(1,
                          7,
                          None,
                          None,
                          22.00) is True
    assert update_listing(7,
                          1,
                          None,
                          None,
                          None) is True
    assert update_listing(1,
                          7,
                          "correct title 1",
                          "this is a correct description",
                          23.00) is True
    assert update_listing(7,
                          1,
                          "correct title 1",
                          "this is a correct description",
                          None) is True
    assert update_listing(1,
                          7,
                          "correct title 1",
                          None,
                          24.00) is True
    assert update_listing(7,
                          1,
                          "correct title 1",
                          None,
                          None) is True
    assert update_listing(1,
                          None,
                          None,
                          "this is a correct description",
                          25.00) is True
    assert update_listing(1,
                          None,
                          None,
                          "this is a correct description",
                          None) is True
    assert update_listing(1,
                          None,
                          None,
                          None,
                          26.00) is True
    assert update_listing(1,
                          None,
                          None,
                          None,
                          None) is True
    assert update_listing(1,
                          None,
                          "correct title 1",
                          "this is a correct description",
                          27.00) is True
    assert update_listing(1,
                          None,
                          "correct title 1",
                          "this is a correct description",
                          None) is True
    assert update_listing(1,
                          None,
                          "correct title 1",
                          None,
                          28.00) is True
    assert update_listing(1,
                          None,
                          "correct title 1",
                          None,
                          None) is True


def test_r5_2_update_listing():
    assert update_listing(2, None, None, None, 19.00) is False
    assert update_listing(2, None, None, None, 20.00) is False
    assert update_listing(2, None, None, None, 21.00) is True


def test_r5_3_update_listing():
    update_listing(3, None, None, None, 19.00)
    assert test_listing_3.last_modified_date == test_date
    update_listing(3, None, None, None, 21.00)
    assert test_listing_3.last_modified_date != test_date


def test_r5_4_update_listing():
    assert update_listing(4,
                          None,
                          "correct title 4",
                          None,
                          None) is True
    assert update_listing(4,
                          None,
                          " incorrect title 4",
                          None,
                          None) is False
    assert update_listing(4,
                          None,
                          " incorrect title 4 ",
                          None,
                          None) is False
    assert update_listing(4,
                          None,
                          "incorrect title 4 ",
                          None,
                          None) is False
    assert update_listing(4,
                          None,
                          "incorrect * title 4",
                          None,
                          None) is False
    title_over_80 = ""
    for i in range(85):
        title_over_80 += 'a'
    assert update_listing(4,
                          None,
                          title_over_80,
                          None,
                          None) is False

    assert update_listing(4,
                          None,
                          None,
                          "This ! is @ a # correct $ description.",
                          None) is True
    assert update_listing(4,
                          None,
                          "T",
                          "Desc",
                          None) is False
    desc_over_2000 = ""
    for i in range(2005):
        desc_over_2000 += 'a'
    assert update_listing(4,
                          None,
                          None,
                          desc_over_2000,
                          None) is False
    assert update_listing(4,
                          None,
                          "This title is greater than 20 characters long",
                          "Description is shorter than title",
                          None) is False

    assert update_listing(4, None, None, None, 5.00) is False
    assert update_listing(4, None, None, None, 10001.00) is False

    temp = test_listing_4.last_modified_date
    temp = temp.replace('-', '')
    temp = int(temp)
    assert 20210102 < temp < 20250102

    assert update_listing(5, None, None, None, 25.00) is False
    assert update_listing(6, None, None, None, 25.00) is False

    assert update_listing(4, None, "listing 2", None, None) is False


db.drop_all()
