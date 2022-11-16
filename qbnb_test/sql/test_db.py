from qbnb.user import register
from pathlib import Path

current_folder = Path(__file__).parent

with open(current_folder.joinpath(
        'test.in')) as my_file:
    test_lines = my_file.readlines()
print(test_lines)


def test_register_email():
    """A test to make sure that there are no injections
       in the email attribute of register()
    """

    # make sure there are no errors thrown
    for line in test_lines:
        register('User', line, 'Password1_')
