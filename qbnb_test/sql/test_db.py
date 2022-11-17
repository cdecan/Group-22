from qbnb.user import register
from qbnb.listing import create_listing
from pathlib import Path

current_folder = Path(__file__).parent

with open(current_folder.joinpath(
        'test.in')) as my_file:
    test_lines = my_file.read().split("\n")

register("Name", "email@email.com", "Password1!")


def test_price():
    """A test to make sure that there are no
    injections in the price attribute of create_listing"""
    # make sure there are no errors thrown
    x = 1
    for line in test_lines:
        create_listing(1, f"Title{x}", "a" * 1999, line)
        x += 1
