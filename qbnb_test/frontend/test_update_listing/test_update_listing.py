from pathlib import Path
import subprocess
from qbnb.user import register
from qbnb.listing import Listing
import time


register('TestUpdateListing', 'tul@test.com', 'Password1_')


# get expected input/output file
current_folder = Path(__file__).parent


def test_R1():
    """
        R1 - One can update all attributes of the listing,
             except owner_id and last_modified_date.

        This requirement is tested using functionality testing.

        Order:
        test update Listing ID.
        test update Title.
        test update Description.
        test update Price.
    """

    # read expected in/out
    expected_in = open(current_folder.joinpath(
        'cases', 'R1', 'test_update_listing.in'))
    expected_out = open(current_folder.joinpath(
        'cases', 'R1', 'test_update_listing.out'), newline="\r\n").read()

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
        R2 - Price can be only increased but cannot be decreased :)

        This requirement is tested using input partition partitioning.

        Order:
        Price is the same
        Price is decreased
        Price is increased
    """

    # read expected in/out
    expected_in = open(current_folder.joinpath(
        'cases', 'R2', 'test_update_listing.in'))
    expected_out = open(current_folder.joinpath(
        'cases', 'R2', 'test_update_listing.out'), newline="\r\n").read()

    print(expected_out)

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip() == expected_out.strip()


def test_R3():
    """
        R3 - last_modified_date should be updated
             when the update operation is successful.

        R3 cannot be tested with only blackbox methods,
           but attempts to follow functionality
           coverage testing.
    """

    to_check_original = Listing.query.filter_by(title='Listing5').first()
    previous_date = to_check_original.last_modified_date

    # read expected in/out
    expected_in = open(current_folder.joinpath(
        'cases', 'R3', 'test_update_listing.in'))
    expected_out = open(current_folder.joinpath(
        'cases', 'R3', 'test_update_listing.out'), newline="\r\n").read()

    print(expected_out)

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip() == expected_out.strip()

    to_check_updated = Listing.query.filter_by(title='Listing5').first()
    updated_date = to_check_updated.last_modified_date

    assert previous_date <= updated_date


def test_R4():
    """
        R4 - The update listing function must follow the same
             requirements as the create listing function.

        This requirement is tested using output partitioning.

        Order Tested:
        Update ID: non int id
                   same id as another listing
                   valid id

        Update Title: invalid title
                      valid title

        Update Description: invalid description
                            valid description

        Update Price: non number price
                      invalid price
                      valid price
    """

    # read expected in/out
    expected_in = open(current_folder.joinpath(
        'cases', 'R4', 'test_update_listing.in'))
    expected_out = open(current_folder.joinpath(
        'cases', 'R4', 'test_update_listing.out'), newline="\r\n").read()

    print(expected_out)

    # pip the input
    output = subprocess.run(
        ['python', '-m', 'qbnb'],
        stdin=expected_in,
        capture_output=True,
    ).stdout.decode()

    print('outputs', output)
    assert output.strip() == expected_out.strip()
