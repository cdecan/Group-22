from os import popen
from pathlib import Path
import subprocess
from flask_sqlalchemy import SQLAlchemy
from qbnb import app
from qbnb.listing import create_listing
from qbnb.user import User

db = SQLAlchemy(app)
user1 = User(email="email@email.com", password="Test123_",
             username="User1", billing_address="",
             postal_code="", balance=100)
user2 = User(email="email1@email.com", password="Test123_", username="User2",
             billing_address="", postal_code="", balance=100)
db.session.add(user1)
db.session.add(user2)
db.session.commit()

# get expected input/output file
current_folder = Path(__file__).parent

# read expected in/out
expected_in = open(current_folder.joinpath(
    'test_update_user_profile.in'))
expected_out = open(current_folder.joinpath(
    'test_update_user_profile.out'), newline="\r\n").read()

print(expected_out)


def test_login():
    """capsys -- object created by pytest to
    capture stdout and stderr"""

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip() == expected_out.strip()

# 2
# email@email.com
# User1
# Test123_
# Test123_
# 2
# email2@email.com
# User2
# Test456_
# Test456_
# Welcome.
# Enter [1] to login.
# Enter [2] to register.
# Enter [3] to exit.
# > Please input email: Please input username: Please input password: Please input the password again: Registration succeeded
# Welcome.
# Enter [1] to login.
# Enter [2] to register.
# Enter [3] to exit.
# > Please input email: Please input username: Please input password: Please input the password again: Registration succeeded


# 1
# email@email.com
# Test123_
# 3
# 1
# newemail@email.com
# 1
# thisemailcannotbeaccepted
#
# bademail@
# bademail@email
# bademail@.com
# @bademail.com
# newemail2@email.com
# 1
# email2@email.com
# newemail3@email.com
# Enter [1] to update email.
# Enter [2] to update username.
# Enter [3] to update billing address.
# Enter [4] to update postal code.
# Enter [end update] to leave.
# > Please enter your new email: Update successful, your email is now newemail@email.com
# Enter [1] to update email.
# Enter [2] to update username.
# Enter [3] to update billing address.
# Enter [4] to update postal code.
# Enter [end update] to leave.
# > Please enter your new email: Email not valid, please try again.
# Please enter your new email: Email not valid, please try again.
# Please enter your new email: Email not valid, please try again.
# Please enter your new email: Email not valid, please try again.
# Please enter your new email: Email not valid, please try again.
# Please enter your new email: Email not valid, please try again.
# Please enter your new email: Update successful, your email is now newemail2@email.com
# Enter [1] to update email.
# Enter [2] to update username.
# Enter [3] to update billing address.
# Enter [4] to update postal code.
# Enter [end update] to leave.
# > Please enter your new email: Email already exists, please try again.
# Please enter your new email: Update successful, your email is now newemail3@email.com