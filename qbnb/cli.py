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
            'Enter [1] to create a listing.'
            'Enter [2] to update a listing.'
            'Enter [3] to update your profile.'
            'Enter [4] to exit.'
            '> ').strip()
        # Check input
        if selection == '1':
            # Create a listing
            # create_listing_page(user_id)
            pass
        elif selection == '2':
            # Update a listing
            # update_listing_page(user_id)
            pass
        elif selection == '3':
            # Update profile
            # update_user_profile()
            pass
        elif selection == '4':
            # Exit
            break
