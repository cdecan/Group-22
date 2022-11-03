from os import popen
from pathlib import Path
import subprocess


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
        'test_create_listing.out'), newline="\r\n").read()

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    # make assertion(s)
    print('outputs', output)
    assert output.strip() == expected_out.strip()
