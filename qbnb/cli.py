# from qbnb.user import login, register
#
#
# def login_page():
#     email = input('Please input email')
#     password = input('Please input password:')
#     return login(email, password)
#
#
# def register_page():
#     email = input('Please input email:')
#     password = input('Please input password:')
#     password_twice = input('Please input the password again:')
#     if password != password_twice:
#         print('password entered not the same')
#     elif register('default name', email, password):
#         print('registration succeeded')
#     else:
#         print('regisration failed.')

from qbnb.listing import Listing, update_listing


def update_listing_page(user_id: int):
    """
    A page which allows the given user to update one of their listings.
    TODO: Split into different functions & make helper functions

    Parameters:
    user_id (int): The unique ID of the current user.

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
        matches = Listing.query.filter_by(title=find_title)  # match title
        to_update = matches.filter_by(owner_id=user_id).first()  # match owner
        if to_update is None:
            print('(You do not have a listing with that title)')
        else:
            found = True
    # Updatable listing found; display menu
    print(f'Now editing \"{to_update}\"')
    id_to_update = to_update.id
    while True:
        selection = input(
            'Enter [1] to update Listing ID. '
            'Enter [2] to update Title.'
            'Enter [3] to update Description.'
            'Enter [4] to update Price.'
            'Enter [5] to exit.'
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
                    print("(Price must be a float)")
            # Update price
            success = update_listing(id_to_update, new_price=new_price)
            print("Updated price." if success else "Update failed.")
        elif selection == '5':
            break
