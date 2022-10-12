from flask_sqlalchemy import SQLAlchemy
from qbnb import app
from qbnb.listing import create_listing
from qbnb.user import User

db = SQLAlchemy(app)
user1 = User(id=1, email="test@test.com", password="asdasd",
             username="asdasd", billing_address="asdasd",
             postal_code="asdasd", balance=5)
user2 = User(id=2, email="", password="password", username="username2",
             billing_address="asdasd", postal_code="asdasd", balance=5)
db.session.add(user1)
db.session.add(user2)
db.session.commit()


def test_r4_1_create_listing():
    '''
    Testing R4-1: If title is not alphanumeric or has
    spaces at the front or back,then it fails.
    '''
    assert create_listing(1, 'TestOne', 'DescriptionDescription', 20.00)\
           is True
    assert create_listing(1, 'Test1', 'DescriptionDescription', 20.00)\
           is True
    assert create_listing(1, 'Test1!', 'DescriptionDescription', 20.00)\
           is False
    assert create_listing(1, 'Test1 ', 'DescriptionDescription', 20.00)\
           is False
    assert create_listing(1, ' Test1', 'DescriptionDescription', 20.00)\
           is False
    assert create_listing(1, ' Test1 ', 'DescriptionDescription', 20.00)\
           is False


def test_r4_2_create_listing():
    '''
    Testing R4-2: If the title of the product is longer than 80 characters
     then it fails.
    '''
    assert create_listing(1, 'Test2', 'DescriptionDescription', 20.00)\
        is True
    assert create_listing(1, 'Titleeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'
                          'eeeeee'
                          'eeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee'
                          'eeeeeeeeeeeeee',
                          'Descriptionnnnnnnnnnnnnnnnnnnnnnnnnnnnn'
                          'nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn'
                          'nnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnnn',
                          20.00) is False


def test_r4_3_create_listing():
    '''
    Testing R4-3: If the description has under 20 or over 2000 characters,
     then it fails
    '''

    assert create_listing(1, 'Test3', 'DescriptionDescription', 20.00)\
           is True
    assert create_listing(1, 'Test32', 'Description', 20.00) is False
    longword = "a"
    for i in range(3000):
        longword += 'a'
    assert create_listing(1, 'Test33', longword, 20.00) is False


def test_r4_4_create_listing():
    '''
    Testing R4-4: If description is shorter than product's title, it fails
    '''

    assert create_listing(1, 'Test4', 'DescriptionDescription', 20.00)\
        is True
    assert create_listing(1, 'TitleTitleTitleTitleTitleTitle'
                             'TitleTitleTitle',
                          'DescriptionDescription', 20.00) is False


def test_r4_5_create_listing():
    '''
    Testing R4-5: If price is lower than 10 or higher than 10,000, it fails
    '''

    assert create_listing(1, 'Test5', 'DescriptionDescription', 20.00)\
           is True
    assert create_listing(1, 'Test52', 'DescriptionDescription', 9.00)\
           is False
    assert create_listing(1, 'Test53', 'DescriptionDescription',
                          10001.00) is False


def test_r4_6_create_listing():
    '''
    Testing R4-6: If last_modified_date is not after 2021-01-02
     and before 2025-01-02, it fails
    '''

    assert create_listing(1, 'Test6', 'DescriptionDescription', 20.00)\
           is True


def test_r4_7_create_listing():
    '''
    Testing R4-7: The corresponding email cannot be empty and must exist
    '''

    assert create_listing(1, 'Test7', 'DescriptionDescription', 20.00)\
           is True
    assert create_listing(2, 'Test72', 'DescriptionDescription', 20.00)\
           is False
    assert create_listing(999, 'Test73', 'DescriptionDescription', 20.00)\
           is False


def test_r4_8_create_listing():
    '''
    Testing r4-8: Two listings cannot have the same title
    '''

    assert create_listing(1, 'Test8', 'DescriptionDescription', 20.00)\
           is True
    assert create_listing(1, 'Test8', 'DescriptionDescription', 20.00)\
           is False


db.drop_all()
