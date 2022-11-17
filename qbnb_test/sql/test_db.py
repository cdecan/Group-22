from qbnb.listing import create_listing
from qbnb.user import register
from pathlib import Path

current_folder = Path(__file__).parent

# Read SQL-injection test lines from file
with open(current_folder.joinpath(
        'test.in')) as my_file:
    test_lines = my_file.read().split('\n')


def test_create_listing_description():
    """
    A test to ensure there are no SQL-injection vulnerabilities in
    the description argument of the create_listing() function.

    Passes if no exceptions are thrown.
    """
    # Ensure there is at least one user (user ID 1 exists)
    register('User', 'SQLListing1@email.com', 'Testing#100')
    # Attempt various injection attacks into description field
    x = 0
    for line in test_lines:
        create_listing(1, f'This is the listing title {x}',
                       line, 100)
    x += 1
