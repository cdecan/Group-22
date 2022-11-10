from pathlib import Path
import subprocess
from qbnb.listing import Listing
from qbnb.user import User
from datetime import date


def test_create_listing():
    """
    Covers all 8 test requirements, using several different
    black-box testing methods. See README.md for details.
    """
    # get expected input/output file
    current_folder = Path(__file__).parent

    # read expected in/out
    expected_in = open(current_folder.joinpath(
        'test_create_listing.in'))
    expected_out = open(current_folder.joinpath(
        'test_create_listing.out'), newline='\r\n').read()

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    # make assertion for in/out
    print('outputs', output)
    assert output.strip() == expected_out.strip()

    # Find the DateAndEmailCheck listing for backend checks
    to_check = Listing.query.filter_by(title='DateAndEmailCheck').first()

    # R4-6: assert date within range
    # TODO: Check for timezone consistency issues
    after = date(2021, 1, 2)
    before = date(2025, 1, 2)
    assert (after < to_check.last_modified_date < before)

    # R4-7: assert owner_email is not empty & exists within database
    owner = User.query.filter_by(id=to_check.owner_id).first()
    assert owner is not None
    assert owner.email != ''
