from os import popen
from pathlib import Path
import subprocess
from qbnb.user import register


register('TestLoginUser', 'tlu@test.com', 'Password1_')


# get expected input/output file
current_folder = Path(__file__).parent


def test_R1():
    """
        R1 - A user can log in using her/his 
             email address and the password.

        This requirement is tested using input partition testing.

        Order:
        !email !Password
        !email password
        email !password
        email password
    """

    # read expected in/out
    expected_in = open(current_folder.joinpath(
        'cases/R1/test_login.in'))
    expected_out = open(current_folder.joinpath(
        'cases/R1/test_login.out'), newline="\r\n").read()

    print(expected_out)
    
    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip() == expected_out.strip()
