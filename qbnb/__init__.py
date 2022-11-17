'''
an init file is required for this folder to be considered as a module
'''
import os
from flask import Flask
# from qbnb.cli import login_page, register_page
app = Flask(__name__)
db_string = os.getenv('db_string')
if db_string:
    app.config['SQLALCHEMY_DATABASE_URI'] = db_string
else:
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()
