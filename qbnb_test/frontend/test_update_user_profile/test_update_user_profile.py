from os import popen
from pathlib import Path
import subprocess

# get expected input/output file
current_folder = Path(__file__).parent

# read expected in/out
expected_in = open(current_folder.joinpath(
    'test_update_user_profile.in'))
expected_out = open(current_folder.joinpath(
    'test_update_user_profile.out'), newline="\r\n").read()

print(expected_out)


def test_update_user_profile():
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
