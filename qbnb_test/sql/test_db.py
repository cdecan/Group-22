from qbnb.listing import create_listing
from pathlib import Path

current_folder = Path(__file__).parent

with open(current_folder.joinpath('test.in')) as my_file:
    test_lines = my_file.readlines()


def test_create_listing_owner_id():
    """A test to make sure that there are no injections
       in the owner_id attribute of create_listing()
    """

    # make sure there are no errors thrown
    n = 1
    for line in test_lines:
        create_listing(line,
                       f'Listing{n}',
                       f'This is a description of Listing{n}',
                       50.0)
        n += 1
