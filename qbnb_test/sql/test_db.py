from qbnb.user import register
from qbnb.listing import create_listing
from pathlib import Path

current_folder = Path(__file__).parent

with open(current_folder.joinpath(
        'test.in')) as my_file:
    test_lines = my_file.readlines()
print(test_lines)


def test_name_password():
    x = 0
    for line in test_lines:
        x += 1
        email = "injection" + str(x) + "@email.com"
        stripped = line.strip()
        register(stripped, email, "Test123")
        register("User", email, stripped)