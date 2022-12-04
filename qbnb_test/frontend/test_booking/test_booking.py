from pathlib import Path
import subprocess
from qbnb.listing import Listing
from qbnb.user import User
from datetime import datetime


def test_booking():
    """
    covering the 4 requirements on frontend testing
    """
    # get expected input/output file
    current_folder = Path(__file__).parent

    # read expected in/out
    expected_in = open(current_folder.joinpath(
        'test_booking.in'))
    expected_out = open(current_folder.joinpath(
        'test_booking.out'), newline='\r\n').read()

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    # make assertion for in/out
    print('outputs', output)
    assert output.strip() == expected_out.strip()
