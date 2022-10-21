from qbnb.user import *


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
        print('Password entered not the same')
    # Create new user
    elif register(username, email, password) == 0:
        print('Registration succeeded')
    # Check for types of failures
    elif register(username, email, password) == 1:
        print('Registration failed: invalid email')
    elif register(username, email, password) == 2:
        print('Registration failed: invalid username')
    elif register(username, email, password) == 3:
        print('Registration failed: invalid password')
    elif register(username, email, password) == 4:
        print('Registration failed: duplicate email')


def user_profile_update_page(user_id):
    action = input("Please enter 1 for updating email, "
                   "2 for updating username, "
                   "3 for updating billing address, "
                   "4 for updating postal code: ")
    action = action.strip()
    if action == 1:
        while True:
            new_email = input("Please enter your new email: ")
            if check_email(new_email):
                existed = User.query.filter_by(email=new_email).all()
                if len(existed) == 0:
                    if update_email(user_id, new_email):
                        print("Update successful, your email is now", new_email)
                        break
                    else:
                        print("Error, user does not exist")
                        break
                else:
                    print("Email already exists, please try again.")
            else:
                print("Email not valid, please try again.")

    elif action == 2:
        while True:
            new_name = input("Please enter your new user name: ")
            if check_name(new_name):
                if update_username(user_id):
                    print("Update successful, your name is now", new_name)
                    break
                else:
                    print("Error, user does not exist")
                    break
            else:
                print("Name is not valid, please try again.")

    elif action == 3:
        new_address = input("Please enter your new address: ")
        if update_billing_address(user_id, new_address):
            print("Update successful, your address is now", new_address)
        else:
            print("Error, user does not exist")

    elif action == 4:
        new_postal_code = input("Please enter your new postal code: ")
        if update_billing_address(user_id, new_postal_code):
            print("Update successful, your address is now", new_postal_code)
        else:
            print("Error, user does not exist")
