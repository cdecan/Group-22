"""
Runs several tests regarding the User entity.

Tests the register and login functions.

Tests the update_username, update_billing_address, update_postal_code,
and update_email functions.
"""
from flask_sqlalchemy import SQLAlchemy
from qbnb.user import User, update_username, update_billing_address
from qbnb.user import update_postal_code, update_email
from qbnb import app
from qbnb.user import register, login

db = SQLAlchemy(app)

user1 = User(id=123, email="test@test.com", password="asdfgh",
             username="asdfgh", billing_address="asdfgh",
             postal_code="A1A 1A1", balance=0)

db.session.add(user1)
db.session.commit()


def test_r3_1_update_user_profile():
    """
    Test R3-1: Ensure that, after upading their username, email,
    billing address, and postal code, that no other attributes
    of the user have changed. If they did, fail.
    """
    # Initial attributes for a user, to be tracked
    orig_id = 234
    orig_email = "test@test.com"
    orig_password = "asdfgh"
    orig_username = "asdfgh"
    orig_billing_address = "asdfgh"
    orig_postal_code = "A1A 1A1"
    orig_balance = 0
    # Create a user to update
    test_user = User(id=orig_id, email=orig_email, password=orig_password,
                     username=orig_username,
                     billing_address=orig_billing_address,
                     postal_code=orig_postal_code, balance=orig_balance)
    # Add user to database
    db.session.add(test_user)
    db.session.commit()
    # Update the username, email, postal code, and billing address of user
    update_username(234, "qwertyu")
    update_billing_address(234, "qwertyu")
    update_postal_code(234, "B1B 1B1")
    update_email(234, "updated@test.com")
    u1 = User.query.filter_by(id=234).first()
    # Ensure the changed values now differ from the original ones
    assert u1.email == orig_email is False
    assert u1.username == orig_username is False
    assert u1.billing_address == orig_billing_address is False
    assert u1.postal_code == orig_postal_code is False
    # Ensure the non-changed values have remained the same
    assert u1.id == orig_id is True
    assert u1.balance == orig_balance is True
    assert u1.password == orig_password is True


def test_r3_2_update_user_profile():
    """
    Test R3-2: Ensure that only a postal code that is non-empty,
    alphanumeric-only, and with no special characters is accepted.
    If not, fail.
    """
    # Test valid code
    assert update_postal_code(123, "B2B 2B2") is True
    # Test empty code
    assert update_postal_code(123, "") is False
    # Test non-alphanumeric and special characters codes
    assert update_postal_code(123, ",.@ %^*") is False
    assert update_postal_code(123, "A1A 1A!") is False


def test_r3_3_update_user_profile():
    """
    Test R3-3: Ensure that only a valid Canadian postal codes are accepted.
    If otherwise, fail.
    """
    # Test valid code
    assert update_postal_code(123, "B2B 2B2") is True
    # Test various invalid Canadian postal codes
    assert update_postal_code(123, "AAA 1A1") is False
    assert update_postal_code(123, "A1A AAA") is False
    assert update_postal_code(123, "111 1A1") is False
    assert update_postal_code(123, "A1A 111") is False
    assert update_postal_code(123, "Invalid A1A 111") is False
    assert update_postal_code(123, "A1A 111 Invalid") is False


def test_r3_4_update_user_profile():
    """
    Test R3-4: Ensure that only usernames that are longer than 2 characters,
    less than 20 characters, non-empty, alphanumeric-only, and does not have
    a space as the prefix or suffix, are accepted. If otherwise, fail.
    """
    # Test valid name
    assert update_username(123, "NormalName") is True
    # Test length <2 and >20
    assert update_username(123, "A") is False
    assert update_username(123, "A" * 21) is False
    # Test empty
    assert update_username(123, "") is False
    # Test non-alphanumeric chars
    assert update_username(123, "!ABC&@#") is False
    # Test spaces as prefix/suffix
    assert update_username(123, " Prefix") is False
    assert update_username(123, "Suffix ") is False


def test_r1_1_user_register():
    """
    Testing if the register function works with r1-1:
    Email cannot be empty. password cannot be empty.
    """
    # testing for username in this block
    assert register('u0', 'user0@test.com', 'Test123_') is True
    assert register('u1', 'user1@test.com', 'Test123_') is True
    # empty name
    assert register('', 'test2@test.com', 'Test123_') is False
    # empty email
    assert register('u2', '', 'Test123_') is False


def test_r1_2_user_register():
    """
    Testing if the register function works with r1-2:
    A user is uniquely identified by his/her user id
    - automatically generated.
    This is done with the login command because id is
    auto generated
    """
    user = login('user0@test.com', 'Test123_')
    assert user is not None
    assert user.id == 3
    user = login('user1@test.com', 'Test123_')
    assert user is not None
    assert user.id == 4


def test_r1_3_user_register():
    """
    Testing if the register function works with r1-3:
    The email has to follow addr-spec defined in RFC 5322
    """
    # illegal email (missing ".")
    assert register('u0', 'test1@testcom', 'Test123_') is False
    # illegal email (multiple @)
    assert register('u0', 'test1@@test.com', 'Test123_') is False
    # illegal email (missing domain after @)
    assert register('u0', 'test1@.com', 'Test123_') is False


def test_r1_4_user_register():
    """
    Testing if the register function works with r1-4:
    Password has to meet the required complexity.
    """
    # Testing password
    assert register('u0', 'p0@test.com', 'Test123_') is True
    # empty password (falls under password too short)
    assert register('u0', 'p1@test.com', '') is False
    # missing special character
    assert register('u0', 'p1@test.com', 'Test123') is False
    # missing number
    assert register('u0', 'p1@test.com', 'Test_') is False
    # missing number and special character
    assert register('u0', 'p1@test.com', 'Test') is False
    # does not have upper case letter
    assert register('u0', 'p1@test.com', 'test_dsak123') is False
    # does not have lower case letter
    assert register('u0', 'p1@test.com', 'TEST123_') is False
    # one that works to prove username and email is valid
    assert register('u0', 'p1@test.com', 'TESTpassword_123*^%') is True
    # illegal email (missing content before @)
    assert register('u0', '@test.com', 'Test123_') is False
    # one that works to prove username and password is valid
    assert register('u0', 'test3@test.com', 'Test123_') is True


def test_r1_5_user_register():
    """
    Testing if the register function works with r1-5:
    Username has to be non-empty, alphanumeric-only,
    and space allowed only if it is not as the prefix or suffix.
    """
    # illegal character
    assert register('u0.', 'test2@test.com', 'Test123_') is False
    # space as a prefix
    assert register(' u0', 'test2@test.com', 'Test123_') is False
    # space as a suffix
    assert register('u0 ', 'test2@test.com', 'Test123_') is False
    # space as a prefix and suffix
    assert register(' u0 ', 'test2@test.com', 'Test123_') is False


def test_r1_6_user_register():
    """
    Testing if the register function works with r1-6:
    Username has to be longer than 2 characters
    and less than 20 characters.
    """
    # name too short
    assert register('X', 'test2@test.com', 'Test123_') is False
    # name too long
    assert register('this is a very long name that the '
                    'program cannot possibly handle',
                    'test2@test.com', 'Test123_') is False
    # different variations of allowed names
    assert register('u 0', 'user2@test.com', 'Test123_') is True
    assert register('u   0', 'user3@test.com', 'Test123_') is True
    assert register('TEST 0', 'user4@test.com', 'Test123_') is True
    assert register('Test', 'user5@test.com', 'Test123_') is True


def test_r1_7_user_register():
    """
    Testing if the register function works with r1-7:
    If the email has been used, the operation failed.
    """
    # testing for email in this block
    assert register('u0', 'test0@test.com', 'Test123_') is True
    assert register('u0', 'test1@test.com', 'Test123_') is True
    # repeated email
    assert register('u0', 'test0@test.com', 'Test123_') is False


def test_r1_8_user_register():
    """
    Testing if the register function works with r1-8:
    Shipping address is empty at the time of registration.
    using login function to test
    """
    user = login('user0@test.com', 'Test123_')
    assert user is not None
    assert user.billing_address == ""


def test_r1_9_user_register():
    """
    Testing if the register function works with r1-9:
    Postal code is empty at the time of registration.
    using login function to test
    """
    user = login('user0@test.com', 'Test123_')
    assert user is not None
    assert user.postal_code == ""


def test_r1_9_user_register():
    """
    Testing if the register function works with r1-9:
    Balance should be initialized as 100
    at the time of registration.
    using login function to test
    """
    user = login('user0@test.com', 'Test123_')
    assert user is not None
    assert user.balance == 100


def test_r2_1_login():
    """
    Testing R2-1: A user can log in using her/his email address
      and the password.
    (will be tested after the previous test,
    so we already have many users in database)
    """

    user = login('user0@test.com', 'Test123_')
    assert user is not None
    assert user.username == 'u0'

    user = login('userthatdontexist@test.com', 'ThisPassword_')
    assert user is None


def test_r2_2_login():
    """
    Testing R2-1: The login function should check
    if the supplied inputs meet the same
    email/password requirements as above,
    before checking the database.
    """

    # invalid email and password
    user = login('@test.com', '1234567')
    assert user is None
    # invalid password
    user = login('test0@test.com', '1234567')
    assert user is None
    # invalid email
    user = login('@test.com', 'Test123_')
    assert user is None


db.drop_all()
