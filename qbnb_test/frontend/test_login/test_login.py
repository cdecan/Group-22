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
        'cases', 'R1', 'test_login.in'))
    expected_out = open(current_folder.joinpath(
        'cases', 'R1', 'test_login.out'), newline="\r\n").read()

    print(expected_out)

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip() == expected_out.strip()


def test_R2():
    """
        R2 - The login function should check if the supplied
             inputs meet the same email/password requirements
             as above, before checking the database.

        This requirement is tested using requirement partitioning.

        R2-1.1 Email cannot be empty
        R2-1.2 Password cannot be empty
        R2-2.1 Email has to follow addr-spec
        R2-3.1 Password is minimum length 6
        R2-3.2 Password has at least one upper case
        R2-3.3 Password has at least one lower case
        R2-3.4 Password has at least one special character
    """

    # read expected in/out
    expected_in = open(current_folder.joinpath(
        'cases', 'R2', 'test_login.in'))
    expected_out = open(current_folder.joinpath(
        'cases', 'R2', 'test_login.out'), newline="\r\n").read()

    print(expected_out)

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip() == expected_out.strip()
