from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# setting up SQLAlchemy and data models
# so we can map data models into database tables
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///db.sqlite'
db = SQLAlchemy(app)


class Listing(db.Model):
    """
    Contains information about the property listings
    """
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String, nullable=False)
    description = db.Column(db.String, nullable=True)
    price = db.Column(db.Float, nullable=False)
    last_modified_date = db.Column(db.Date, nullable=False)
    owner_id = db.Column(db.Integer, db.ForeignKey('owner.id'),
                         nullable=False)
    owner = db.relationship('Listing', backref=db.backref('listings',
                                                          lazy=True))

    def __repr__(self):
        """A listing represents itself by displaying the associated title"""
        return '<Listing %r>' % self.title


def create_listing(owner_id, title, description, price):
    # get the user posting the listing
    user = User.query.get(owner_id)
    # check if user email exists
    email_existed = User.query.filter_by(user=user, email=user.email).all()
    if len(email_existed) > 0:
        return False
    # check if title meets criteria:
    if len(title) < 1 or len(title) > 80:
        return False
    if not title.isalnum() or title.endswith(' ') or title.startswith(' '):
        return False
    title_existed = Listing.query.filter_by(title=title)
    if len(title_existed) > 0:
        return False
    # check if description meets criteria:
    if len(description) < 20 or len(description) > 2000 \
            or len(description) < len(title):
        return False
    # check if price meets criteria:
    if price < 10 or price > 10000:
        return False
    # product was just created
    last_modified_date = date.today()

    # listing is ok -> make listing
    listing = Listing(title=title, description=description, price=price,
                      last_modified_date=last_modified_date, owner_id=owner_id)

