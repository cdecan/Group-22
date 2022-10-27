from qbnb.listing import create_listing, Listing, update_listing
from qbnb.user import *


def user_login_page():
    """
    This function prompts the user to enter their login details
    and attempts to log them in using their input.

    Returns:
        User or None: Returns the user if the login was
                      successful and None otherwise
    """

    # Gets user input
    email = input('Please input email: ')
    password = input('Please input password: ')

    # Attempts to login
    success = login(email, password)

    # Informs the user about the login status
    if success is not None:
        print('Login successful')
    else:
        print('Login failed, incorrect email or password')

    # Returns the user if login was successful and None otherwise
    return success


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


def home_page(user_id: int):
    """
    Displays the home page. Gives the user the option to access the listing
    creation, listing update, and profile update pages.

    Parameters:
        user_id (int): The unique ID of the calling user

    Returns:
        None
    """
    # Prompt user for user
    while True:
        selection = input(
            'Enter [1] to create a listing.\n'
            'Enter [2] to update a listing.\n'
            'Enter [3] to update your profile.\n'
            'Enter [4] to exit.\n'
            '> ').strip()
        # Check input
        if selection == '1':
            # Create a listing
            create_listing_page(user_id)
        elif selection == '2':
            # Update a listing
            update_listing_page(user_id)
        elif selection == '3':
            # Update profile
            user_profile_update_page(user_id)
        elif selection == '4':
            # Exit
            break


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
                    if update_username(user_id, new_name):
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


def update_listing_page(user_id: int):
    """
    A page which allows the given user to update one of their listings.

    Parameters:
        user_id (int): The unique ID of the current user

    Returns:
        bool: True if update was successful, False otherwise
    """
    # Print greeting
    print('Leave the below field empty to return.')
    found = False
    while not found:
        # Request title from user
        find_title = input('Enter title of listing to edit: ')

        # Exit if blank title was given
        if find_title == '':
            return False

        # Find the listing and ensure its owned by this user
        to_update = Listing.query.filter_by(title=find_title,
                                            owner_id=user_id).first()
        if to_update is None:
            print('(You do not have a listing with that title)')
        else:
            found = True
    # Updatable listing found; display menu
    print(f'Now editing \"{to_update}\"')
    id_to_update = to_update.id
    while True:
        selection = input(
            'Enter [1] to update Listing ID.\n'
            'Enter [2] to update Title.\n'
            'Enter [3] to update Description.\n'
            'Enter [4] to update Price.\n'
            'Enter [5] to exit.\n'
            '>').strip()

        if selection == '1':
            # Request new id from user (ensure int)
            valid = False
            while not valid:
                new_id = input('Enter a new listing ID: ')
                # Ensure ID is int
                try:
                    new_id = int(new_id)
                    valid = True
                except ValueError:
                    print("(ID must be an integer)")

            # Update ID
            success = update_listing(id_to_update, new_id=new_id)
            if success:
                print("Updated listing ID.")
                # Note the new ID
                id_to_update = new_id
            else:
                print("Update failed.")

        elif selection == '2':
            # Request new title from user
            new_title = input('Enter a new title: ')

            # Update title
            success = update_listing(id_to_update, new_title=new_title)
            print("Updated title." if success else "Update failed.")

        elif selection == '3':
            # Request new description from user
            new_desc = input('Enter a new description: ')

            # Update description
            success = update_listing(id_to_update, new_description=new_desc)
            print("Updated description." if success else "Update failed.")

        elif selection == '4':
            # Request new price from user (ensure float)
            valid = False
            while not valid:
                new_price = input('Enter a new price: ')
                # Ensure ID is int
                try:
                    new_price = float(new_price)
                    valid = True
                except ValueError:
                    print("(Price must be a number)")
            # Update price
            success = update_listing(id_to_update, new_price=new_price)
            print("Updated price." if success else "Update failed.")

        elif selection == '5':
            break
