'''
an init file is required for this folder to be considered as a module
'''
from flask import Flask
# From qbnb.cli import login_page, register_page
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../db.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.app_context().push()
