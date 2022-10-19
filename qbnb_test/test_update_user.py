from flask_sqlalchemy import SQLAlchemy
from qbnb.user import User, update_username, update_billing_address
from qbnb.user import update_postal_code, update_email
from qbnb import app
import qbnb.user

db = SQLAlchemy(app)

user1 = User(id=10, email="sample10@test.com", password="asdfgh",
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
    # Note the initial attributes of this user, for comparison later
    orig_id = user1.id
    orig_email = user1.email
    orig_password = user1.password
    orig_username = user1.username
    orig_billing_address = user1.billing_address
    orig_postal_code = user1.postal_code
    orig_balance = user1.balance
    # Update the username, email, postal code, and billing address of user
    update_username(user1.id, "qwertyu")
    update_billing_address(user1.id, "qwertyu")
    update_postal_code(user1.id, "B1B 1B1")
    update_email(user1.id, "updated@test.com")
    u1 = User.query.filter_by(id=user1.id).first()
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
    assert update_postal_code(10, "B2B 2B2") is True
    # Test empty code
    assert update_postal_code(10, "") is False
    # Test non-alphanumeric and special characters codes
    assert update_postal_code(10, ",.@ %^*") is False
    assert update_postal_code(10, "A1A 1A!") is False


def test_r3_3_update_user_profile():
    """
    Test R3-3: Ensure that only a valid Canadian postal codes are accepted.
    If otherwise, fail.
    """
    # Test valid code
    assert update_postal_code(10, "B2B 2B2") is True
    # Test various invalid Canadian postal codes
    assert update_postal_code(10, "AAA 1A1") is False
    assert update_postal_code(10, "A1A AAA") is False
    assert update_postal_code(10, "111 1A1") is False
    assert update_postal_code(10, "A1A 111") is False
    assert update_postal_code(10, "Invalid A1A 111") is False
    assert update_postal_code(10, "A1A 111 Invalid") is False


def test_r3_4_update_user_profile():
    """
    Test R3-4: Ensure that only usernames that are longer than 2 characters,
    less than 20 characters, non-empty, alphanumeric-only, and does not have
    a space as the prefix or suffix, are accepted. If otherwise, fail.
    """
    # Test valid name
    assert update_username(10, "NormalName") is True
    # Test length <2 and >20
    assert update_username(10, "A") is False
    assert update_username(10, "A" * 21) is False
    # Test empty
    assert update_username(10, "") is False
    # Test non-alphanumeric chars
    assert update_username(10, "!ABC&@#") is False
    # Test spaces as prefix/suffix
    assert update_username(10, " Prefix") is False
    assert update_username(10, "Suffix ") is False
