from flask_sqlalchemy import SQLAlchemy
from qbnb.listing import Listing
from qbnb.listing import update_listing
import datetime
from qbnb import app

db = SQLAlchemy(app)


test_date = datetime.datetime(2021, 8, 5)
test_listing_1 = Listing(id=11,
                         title="listing 1",
                         description="description",
                         price=20.00,
                         last_modified_date=test_date,
                         owner_id=1)
test_listing_2 = Listing(id=12,
                         title="listing 2",
                         description="description",
                         price=20.00,
                         last_modified_date=test_date,
                         owner_id=1)
test_listing_3 = Listing(id=13,
                         title="listing 3",
                         description="description",
                         price=20.00,
                         last_modified_date=test_date,
                         owner_id=1)
test_listing_4 = Listing(id=14,
                         title="listing 4",
                         description="descriptiondescriptiondescription",
                         price=20.00,
                         last_modified_date=test_date,
                         owner_id=1)
test_listing_5 = Listing(id=15,
                         title="listing 5",
                         description="description",
                         price=20.00,
                         last_modified_date=test_date,
                         owner_id=2)
test_listing_6 = Listing(id=16,
                         title="listing 6",
                         description="description",
                         price=20.00,
                         last_modified_date=test_date,
                         owner_id=999)
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

    assert update_listing(11,
                          50,
                          None,
                          "this is a correct description",
                          21.00) is True
    assert update_listing(50,
                          11,
                          None,
                          "this is a correct description",
                          None) is True
    assert update_listing(11,
                          50,
                          None,
                          None,
                          22.00) is True
    assert update_listing(50,
                          11,
                          None,
                          None,
                          None) is True
    assert update_listing(11,
                          50,
                          "correct title 1 0",
                          "this is a correct description",
                          23.00) is True
    assert update_listing(50,
                          11,
                          "correct title 1 1",
                          "this is a correct description",
                          None) is True
    assert update_listing(11,
                          50,
                          "correct title 1 2",
                          None,
                          24.00) is True
    assert update_listing(50,
                          11,
                          "correct title 1 3",
                          None,
                          None) is True
    assert update_listing(11,
                          None,
                          None,
                          "this is a correct description",
                          25.00) is True
    assert update_listing(11,
                          None,
                          None,
                          "this is a correct description",
                          None) is True
    assert update_listing(11,
                          None,
                          None,
                          None,
                          26.00) is True
    assert update_listing(11,
                          None,
                          None,
                          None,
                          None) is True
    assert update_listing(11,
                          None,
                          "correct title 1 4",
                          "this is a correct description",
                          27.00) is True
    assert update_listing(11,
                          None,
                          "correct title 1 5",
                          "this is a correct description",
                          None) is True
    assert update_listing(11,
                          None,
                          "correct title 1 6",
                          None,
                          28.00) is True
    assert update_listing(11,
                          None,
                          "correct title 1 7",
                          None,
                          None) is True


def test_r5_2_update_listing():
    """
        Testing R5-2: Testing that the price can only be increased.
    """

    assert update_listing(12, None, None, None, 19.00) is False
    assert update_listing(12, None, None, None, 20.00) is False
    assert update_listing(12, None, None, None, 21.00) is True


def test_r5_3_update_listing():
    """
        Testing R5-3: Checks if last_modified_date is
        updated when the update operation is successful.
    """

    update_listing(13, None, None, None, 19.00)
    check_date = Listing.query.filter_by(id=13).first()
    assert check_date.last_modified_date == test_date
    update_listing(13, None, None, None, 25.00)
    check_date = Listing.query.filter_by(id=13).first()
    assert check_date.last_modified_date != test_date
    # assert tf is False


def test_r5_4_update_listing():
    """
        Testing R5-4: Checks in order if the
        updates made follow the requirements in R4.
    """

    # R4-1 and R4-2
    assert update_listing(14,
                          None,
                          "correct title 4",
                          None,
                          None) is True
    assert update_listing(14,
                          None,
                          " incorrect title 4",
                          None,
                          None) is False
    assert update_listing(14,
                          None,
                          " incorrect title 4 ",
                          None,
                          None) is False
    assert update_listing(14,
                          None,
                          "incorrect title 4 ",
                          None,
                          None) is False
    assert update_listing(14,
                          None,
                          "incorrect * title 4",
                          None,
                          None) is False
    title_over_80 = ""
    for i in range(85):
        title_over_80 += 'a'
    assert update_listing(14,
                          None,
                          title_over_80,
                          None,
                          None) is False

    # R4-3 and R4-4
    assert update_listing(14,
                          None,
                          None,
                          "This ! is @ a # correct $ description.",
                          None) is True
    assert update_listing(14,
                          None,
                          "",
                          "Desc",
                          None) is False
    desc_over_2000 = ""
    for i in range(2005):
        desc_over_2000 += 'a'
    assert update_listing(14,
                          None,
                          None,
                          desc_over_2000,
                          None) is False
    assert update_listing(14,
                          None,
                          "This title is greater than 20 characters long",
                          "Description is shorter than title",
                          None) is False

    # R4-5
    assert update_listing(14, None, None, None, 5.00) is False
    assert update_listing(14, None, None, None, 10001.00) is False

    # R4-6
    temp = Listing.query.filter_by(id=14).first()
    temp = temp.last_modified_date
    lower_bound = datetime.datetime(2021, 1, 2)
    upper_bound = datetime.datetime(2025, 1, 1, 23, 59, 59)
    assert lower_bound <= temp <= upper_bound

    # R4-7
    assert update_listing(15, None, None, None, 25.00) is False
    assert update_listing(16, None, None, None, 25.00) is False

    # R4-8
    assert update_listing(14, None, "listing 2", None, None) is False
