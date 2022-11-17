from qbnb.listing import create_listing
from qbnb.user import register
from pathlib import Path

current_folder = Path(__file__).parent

# Read SQL-injection test lines from file
with open(current_folder.joinpath('test.in')) as my_file:
    test_lines = my_file.read().split('\n')

# Ensure there is at least one user (user ID 1 exists)
register("Name", "sqlTestEmail@email.com", "Password1!")

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


def test_name():
    """
    testing injection for register function with name being different input
    requires no input and returns nothing
    """
    x = 0
    for line in test_lines:
        x += 1
        email = f"injection_name{x}@email.com"
        register(line, email, "Test123_")


def test_password():
    """
    testing injection for register function with password being different input
    requires no input and returns nothing
    """
    x = 0
    for line in test_lines:
        x += 1
        email = f"injection_password{x}@email.com"
        register("User", email, line)


def test_create_listing_description():
    """
    A test to ensure there are no SQL-injection vulnerabilities in
    the description argument of the create_listing() function.

    Passes if no exceptions are thrown.
    """
    # Attempt various injection attacks into description field
    x = 0
    for line in test_lines:
        create_listing(1, f'This is the listing title {x}',
                       line, 100)
        x += 1


def test_title():
    """A test to make sure that there are no
    injections in the title attribute of create_listing"""
    # make sure there are no errors thrown
    for line in test_lines:
        create_listing(1, line, "a" * 1999, 50.0)
