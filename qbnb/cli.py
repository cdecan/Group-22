from qbnb.user import login, register


def login_page():
    email = input('Please input email')
    password = input('Please input password:')
    return login(email, password)


def register_page():
    # Get the attributes required for creating a user
    email = input('Please input email: ')
    username = input('Please input username: ')
    password = input('Please input password: ')
    password_twice = input('Please input the password again: ')
    if password != password_twice:
        print('password entered not the same')
    # Create new user
    elif register(username, email, password) == 0:
        print('registration succeeded')
    # Check for types of failures
    elif register(username, email, password) == 1:
        print('registration failed: invalid email')
    elif register(username, email, password) == 2:
        print('registration failed: invalid username')
    elif register(username, email, password) == 3:
        print('registration failed: invalid password')
