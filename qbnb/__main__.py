from qbnb import *
from qbnb.models import *
from qbnb.listing import *
from qbnb.review import *
from qbnb.booking import *
from qbnb.user import *
from qbnb.cli import login_page, register_page


def main():
    while True:
        selection = input(
            'Welcome. Please type 1 to login. '
            'Or type 2 register. Or type 3 to exit')
        selection = selection.strip()
        if selection == '1':
            user = login_page()
            if user:
                print(f'welcome {user.username}')
                break
            else:
                print('login failed')
        elif selection == '2':
            register_page()
        elif selection == '3':
            break


if __name__ == '__main__':
    main()
