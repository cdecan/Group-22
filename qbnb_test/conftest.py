import os
from qbnb import app


'''
This file defines what to do BEFORE running any test cases:


'''


def pytest_sessionstart():
    with app.app_context():
        '''
        Delete database file if existed. So testing can start fresh.
        '''
        print('Setting up environment..')
        db_file = 'db.sqlite'
        if os.path.exists(db_file):
            os.remove(db_file)


def pytest_sessionfinish():
    with app.app_context():
        '''
        Optional function called when testing is done.
        Do nothing for now
        '''
        pass
