from qbnb.listing import create_listing
from pathlib import Path

current_folder = Path(__file__).parent

# Read SQL-injection test lines from file
with open(current_folder.joinpath(
        'test.in')) as my_file:
    test_lines = my_file.readlines()


def test_create_listing_description():
    """
    A test to ensure there are no SQL-injection vulnerabilities in
    the description argument of the create_listing() function.
    """
    # Attempt various injection attacks into description field
    # Passes if no exceptions are thrown.
    id = 0
    for line in test_lines:
        create_listing(id, "This is a valid listing title",
                       line, 100)
        id += 1  # (ensure owner_id is always unique)
