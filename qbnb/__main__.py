from qbnb import *
from qbnb.listing import *
from qbnb.review import *
from qbnb.booking import *
from qbnb.user import *
from qbnb.cli import *


def main():
    while True:
        selection = input(
            'Welcome.'
            'Enter [1] to login.'
            'Enter [2] to register.'
            'Enter [3] to exit.'
            '> ')
        selection = selection.strip()
        if selection == '1':
            user = user_login_page()
            if user:
                print(f'Welcome, {user.username}.')
                home_page(user.id)
            else:
                print('Login failed.')
        elif selection == '2':
            register_page()
        elif selection == '3':
            break


if __name__ == '__main__':
    main()
