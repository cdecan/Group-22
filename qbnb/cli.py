from qbnb.listing import create_listing
from qbnb.user import login, register


def login_page():
    email = input('Please input email')
    password = input('Please input password:')
    return login(email, password)


def register_page():
    """
    An page which allows a person to create (register) a user.

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


def create_listing_page(user_id: int):
    """
    An page which allows the current user to create a listing.

    Parameters:
        user_id (int): The unique ID of the current user.

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
