class User:
    """
    This class consists of all the user info and methods about balances
    """
    def __init__(self, name, balance, bank_info, user_id=-1, transactions=[], reviews=[], listings=[]):
        """This function initializes the user data"""
        self.name = name
        self.balance = balance
        self.bank_info = bank_info
        self.user_id = user_id
        self.transactions = transactions
        self.reviews = reviews
        self.listings = listings

    def add_transaction(self, Transaction):
        """This function adds a transaction to the list of transactions"""
        self.transactions.append(Transaction)

    def add_review(self, Review):
        """This function adds a review to the list of reviews"""
        self.reviews.append(Review)

    def add_listing(self, Listing):
        """This function adds a listing to the list of listing"""
        self.listings.append(Listing)

    def set_user_id(self, user_id):
        """This function sets the user id to a specific id"""
        self.user_id = user_id

    def get_id(self):
        """This function returns the user id"""
        return self.user_id

    def get_balance(self):
        """This function returns the balance of the user"""
        return self.balance

    def get_bank_info(self):
        """This function returns the banking info of the user"""
        return self.bank_info

    def get_transaction_history(self):
        """This function returns the transactions of the user as a list"""
        return self.transactions

    def get_review_history(self):
        """This function returns the reviews from the user as a list"""
        return self.reviews

    def get_listing_history(self):
        """This function returns the listings from the user as a list"""
        return self.listings
