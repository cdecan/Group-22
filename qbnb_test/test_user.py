from flask_sqlalchemy import SQLAlchemy
from qbnb.user import register, login
from qbnb import app


db = SQLAlchemy(app)
db.session.commit()


def test_r1_1_user_register():
    """
    Testing if the register function works with r1-1:
    Email cannot be empty. password cannot be empty.
    """
    # testing for username in this block
    assert register('u0', 'user0@test.com', 'Test123_') == 0
    assert register('u1', 'user1@test.com', 'Test123_') == 0
    # empty name
    assert register('', 'test2@test.com', 'Test123_') != 0
    # empty email
    assert register('u2', '', 'Test123_') != 0


def test_r1_2_user_register():
    """
    Testing if the register function works with r1-2:
    A user == uniquely identified by his/her user id
    - automatically generated.
    This == done with the login command because id is
    auto generated
    """
    user = login('user0@test.com', 'Test123_')
    assert user is not None
    assert user.id == 4
    user = login('user1@test.com', 'Test123_')
    assert user is not None
    assert user.id == 5


def test_r1_3_user_register():
    """
    Testing if the register function works with r1-3:
    The email has to follow addr-spec defined in RFC 5322
    """
    # illegal email (missing ".")
    assert register('u0', 'test1@testcom', 'Test123_') != 0
    # illegal email (multiple @)
    assert register('u0', 'test1@@test.com', 'Test123_') != 0
    # illegal email (missing domain after @)
    assert register('u0', 'test1@.com', 'Test123_') != 0


def test_r1_4_user_register():
    """
    Testing if the register function works with r1-4:
    Password has to meet the required complexity.
    """
    # Testing password
    assert register('u0', 'p0@test.com', 'Test123_') == 0
    # empty password (falls under password too short)
    assert register('u0', 'p1@test.com', '') != 0
    # missing special character
    assert register('u0', 'p1@test.com', 'Test123') != 0
    # missing number
    assert register('u0', 'p1@test.com', 'Test_') != 0
    # missing number and special character
    assert register('u0', 'p1@test.com', 'Test') != 0
    # does not have upper case letter
    assert register('u0', 'p1@test.com', 'test_dsak123') != 0
    # does not have lower case letter
    assert register('u0', 'p1@test.com', 'TEST123_') != 0
    # one that works to prove username and email == valid
    assert register('u0', 'p1@test.com', 'TESTpassword_123*^%') == 0
    # illegal email (missing content before @)
    assert register('u0', '@test.com', 'Test123_') != 0
    # one that works to prove username and password == valid
    assert register('u0', 'test3@test.com', 'Test123_') == 0


def test_r1_5_user_register():
    """
    Testing if the register function works with r1-5:
    Username has to be non-empty, alphanumeric-only,
    and space allowed only if it !=  as the prefix or suffix.
    """
    # illegal character
    assert register('u0.', 'test2@test.com', 'Test123_') != 0
    # space as a prefix
    assert register(' u0', 'test2@test.com', 'Test123_') != 0
    # space as a suffix
    assert register('u0 ', 'test2@test.com', 'Test123_') != 0
    # space as a prefix and suffix
    assert register(' u0 ', 'test2@test.com', 'Test123_') != 0


def test_r1_6_user_register():
    """
    Testing if the register function works with r1-6:
    Username has to be longer than 2 characters
    and less than 20 characters.
    """
    # name too short
    assert register('X', 'test2@test.com', 'Test123_') != 0
    # name too long
    assert register('this == a very long name that the '
                    'program cannot possibly handle',
                    'test2@test.com', 'Test123_') != 0
    # different variations of allowed names
    assert register('u 0', 'user2@test.com', 'Test123_') == 0
    assert register('u   0', 'user3@test.com', 'Test123_') == 0
    assert register('TEST 0', 'user4@test.com', 'Test123_') == 0
    assert register('Test', 'user5@test.com', 'Test123_') == 0


def test_r1_7_user_register():
    """
    Testing if the register function works with r1-7:
    If the email has been used, the operation failed.
    """
    # testing for email in this block
    assert register('u0', 'test0@test.com', 'Test123_') == 0
    assert register('u0', 'test1@test.com', 'Test123_') == 0
    # repeated email
    assert register('u0', 'test0@test.com', 'Test123_') != 0


def test_r1_8_user_register():
    """
    Testing if the register function works with r1-8:
    Shipping address == empty at the time of registration.
    using login function to test
    """
    user = login('user0@test.com', 'Test123_')
    assert user is not None
    assert user.billing_address == ""


def test_r1_9_user_register():
    """
    Testing if the register function works with r1-9:
    Postal code == empty at the time of registration.
    using login function to test
    """
    user = login('user0@test.com', 'Test123_')
    assert user is not None
    assert user.postal_code == ""


def test_r1_10_user_register():
    """
    Testing if the register function works with r1-10:
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
