from os import popen
from pathlib import Path
import subprocess
from qbnb.user import login

# get expected input/output file
current_folder = Path(__file__).parent


def test_register_r1():
    """R1 - email cannot be empty, password cannot be empty.
    Tested with exhaustive output coverage"""

    # read expected in/out
    expected_in = open(current_folder.joinpath(
        'R1/test_register.in'))
    expected_out = open(current_folder.joinpath(
        'R1/test_register.out'), newline="\r\n").read()

    print(expected_out)

    # OUTPUTS RELATED TO EMAIL:

    # OUTPUT 1: Registration succeeded

    # OUTPUT 2: Registration failed: invalid email

    # OUTPUT 3: Registration failed: duplicate email

    # OUTPUTS RELATED TO PASSWORD:

    # OUTPUT 4: Registration failed: invalid password

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip() == expected_out.strip()


def test_register_r2():
    """R1-2: A user is uniquely identified by his/her user id.
    """

    # userID is unique so if two users are able to exist,
    # then they must have unique IDs
    # read expected in/out
    expected_in = open(current_folder.joinpath(
        'R2/test_register.in'))
    expected_out = open(current_folder.joinpath(
        'R2/test_register.out'), newline="\r\n").read()

    print(expected_out)

    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip() == expected_out.strip()


def test_register_r3():
    """R1-3: The email has to follow addr-spec defined in RFC 5322
    Tested with input partitioning"""

    # P1: Local part is empty | @ is not there | Domain is empty
    # P2: Local part is empty | @ is not there | Domain is not empty but no .
    # P3: Local part is empty | @ is not there | Domain is not empty and has .
    # P4: Local part is empty | @ is there | Domain is empty
    # P5: Local part is empty | @ is there | Domain is not empty but no .
    # P6: Local part is empty | @ is there | Domain is not empty and has .
    # P7: Local part is there | @ is not there | Domain is empty
    # P8: Local part is there | @ is not there | Domain is not empty but no .
    # P9: Local part is there | @ is not there | Domain is not empty and has .
    # P10: Local part is there | @ is there | Domain is empty
    # P11: Local part is there | @ is there | Domain is not empty but no .
    # P12: Local part is there | @ is there | Domain is not empty and has .

    # read expected in/out
    expected_in = open(current_folder.joinpath(
        'R3/test_register.in'))
    expected_out = open(current_folder.joinpath(
        'R3/test_register.out'), newline="\r\n").read()

    print(expected_out)

    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip() == expected_out.strip()


def test_register_r4():
    """R1-4: Password has to meet the required complexity: minimum length 6,
    at least one upper case, at least one lower case,
    and at least one special character.
    Tested with input partitioning"""

    # P1: too short | no upper | no lower | no special
    # P2: too short | has upper | no lower | no special
    # P3: too short | no upper | has lower | no special
    # P4: too short | no upper | no lower | has special
    # P5: too short | has upper | has lower | no special
    # P6: too short | has upper | no lower | has special
    # P7: too short | no upper | has lower | has special
    # P8: too short | has upper | has lower | has special

    # P9: good length | no upper | no lower | no special
    # P10: good length | has upper | no lower | no special
    # P11: good length | no upper | has lower | no special
    # P12: good length | no upper | no lower | has special
    # P13: good length | has upper | has lower | no special
    # P14: good length | has upper | no lower | has special
    # P15: good length | no upper | has lower | has special
    # P16: good length | has upper | has lower | has special

    # read expected in/out
    expected_in = open(current_folder.joinpath(
        'R4/test_register.in'))
    expected_out = open(current_folder.joinpath(
        'R4/test_register.out'), newline="\r\n").read()

    print(expected_out)

    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip() == expected_out.strip()


def test_register_r5():
    """R1-5: Username has to be non-empty, alphanumeric-only,
    and space allowed only if it is not as the prefix or suffix.
    Tested with input partitioning"""

    # P1: name empty
    # P2: non-alphanumeric | spaces at ends
    # P3: non-alphanumeric | spaces in middle
    # P4: alphanumeric | spaces at ends
    # P5: alphanumeric | spaces in middle

    # read expected in/out
    expected_in = open(current_folder.joinpath(
        'R5/test_register.in'))
    expected_out = open(current_folder.joinpath(
        'R5/test_register.out'), newline="\r\n").read()

    print(expected_out)

    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip() == expected_out.strip()


def test_register_r6():
    """R1-6: Username has to be longer than 2 characters
    and less than 20 characters.
    Tested with input boundary testing"""

    # B1: " "
    # B2: "aa"
    # B3: "aaaaaaaaaaaaaaaaaaaa"

    # read expected in/out
    expected_in = open(current_folder.joinpath(
        'R6/test_register.in'))
    expected_out = open(current_folder.joinpath(
        'R6/test_register.out'), newline="\r\n").read()

    print(expected_out)

    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip() == expected_out.strip()


def test_register_r7():
    """R1-7: If the email has been used, the operation failed."""

    # read expected in/out
    expected_in = open(current_folder.joinpath(
        'R7/test_register.in'))
    expected_out = open(current_folder.joinpath(
        'R7/test_register.out'), newline="\r\n").read()

    print(expected_out)

    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip() == expected_out.strip()


def test_register_r8():
    """R1-8: Shipping address is empty at the time of registration."""

    # read expected in/out
    expected_in = open(current_folder.joinpath(
        'R8/test_register.in'))

    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    user = login('testreg8@test.com', 'Test123!')

    print('outputs', output)
    assert user is not None
    assert user.billing_address == ""


def test_register_r9():
    """R1-9: Postal code is empty at the time of registration."""

    # read expected in/out
    expected_in = open(current_folder.joinpath(
        'R9/test_register.in'))

    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    user = login('testreg9@test.com', 'Test123!')

    print('outputs', output)
    assert user is not None
    assert user.postal_code == ""


def test_register_r10():
    """R1-10: Balance should be initialized as 100
     at the time of registration. (free $100 dollar signup bonus)."""

    # read expected in/out
    expected_in = open(current_folder.joinpath(
        'R10/test_register.in'))

    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    user = login('testreg10@test.com', 'Test123!')

    print('outputs', output)
    assert user is not None
    assert user.balance == 100
