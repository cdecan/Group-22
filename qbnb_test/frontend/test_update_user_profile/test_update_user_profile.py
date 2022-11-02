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

