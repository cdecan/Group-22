from qbnb.listing import create_listing
from qbnb.user import *


def login_page():
    email = input('Please input email')
    password = input('Please input password:')
    return login(email, password)


def register_page():
    """
    A page which allows a person to create (register) a user.

    Parameters:
        None

    Returns:
        None
    """
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
    """
    This function allows a user to change their profile.

    Parameters:
        user_id(int): The unique id of user
    Returns:
        None
    """
    print('After you have made your selection, '
          'if you enter \"update selection\" '
          'you will be able to '
          'return to selection page again')
    while True:
        action = input('Please enter 1 for updating email, '
                       '2 for updating username, '
                       '3 for updating billing address, '
                       '4 for updating postal code,'
                       '\"end update\"to leave: ')
        if action == 'end update':
            break
        action = action.strip()
        # if selected changing email
        if action == '1':
            while True:
                new_email = input('Please enter your new email: ')
                # if user wants to go back to selection
                if new_email == 'update selection':
                    break
                # checking if it is a valid email
                if check_email(new_email):
                    # checking for dupe emails
                    existed = User.query.filter_by(email=new_email).all()
                    if len(existed) == 0:
                        if update_email(user_id, new_email):
                            print('Update successful, '
                                  'your email is now', new_email)
                            break
                        else:
                            print('Error, user does not exist.')
                            break
                    else:
                        print('Email already exists, please try again.')
                else:
                    print('Email not valid, please try again.')

        # if selected changing username
        elif action == '2':
            while True:
                new_name = input('Please enter your new user name: ')
                # if user wants to go back to selection
                if new_name == 'update selection':
                    break
                # checking if name is valid
                if check_name(new_name):
                    if update_username(user_id):
                        print('Update successful, '
                              'your name is now', new_name)
                        break
                    else:
                        print('Error, user does not exist.')
                        break
                else:
                    print('Name is not valid, please try again.')

        # if selected changing address
        elif action == '3':
            new_address = input('Please enter your new address: ')
            # if user wants to go back to selection
            if new_address == 'update selection':
                break
            if update_billing_address(user_id, new_address):
                print('Update successful, '
                      'your address is now', new_address)
            else:
                print('Error, user does not exist.')

        # if selected changing postal code
        elif action == '4':
            new_postal_code = input('Please enter your new postal code: ')
            # if user wants to go back to selection
            if new_postal_code == 'update selection':
                break
            if update_postal_code(user_id, new_postal_code):
                print('Update successful, '
                      'your postal code is now', new_postal_code)
            else:
                print('Error, user does not exist '
                      'or postal code does not meet requirements.')


def create_listing_page(user_id: int):
    """
    A page which allows the current user to create a listing.

    Parameters:
        user_id (int): The unique ID of the current user

    Returns:
        bool: True if the listing creation was successful, False otherwise
    """
    # Request title from user
    title = input('Enter listing title: ')
    # Request description from user
    description = input('Enter listing description: ')
    # Request price from user (with error checking)
    price_ok = False
    while not price_ok:
        price = input('Enter listing price: $')
        # Ensure price is float
        try:
            price = float(price)
            price_ok = True
        except ValueError:
            print("(Please enter a float for price)")
    # Attempt to create listing with given data
    success = create_listing(user_id, title, description, price)
    if success:
        print(f'Listing \"{title}\" was created successfully.')
        return True
    else:
        print('Failed to create listing.')
        return False
