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
