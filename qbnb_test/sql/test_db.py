from qbnb.user import register
from qbnb.listing import create_listing
from pathlib import Path

current_folder = Path(__file__).parent

with open(current_folder.joinpath(
        'test.in')) as my_file:
    test_lines = my_file.read().split("\n")


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
