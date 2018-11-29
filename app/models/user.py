"""user module
"""
import random
import string

from werkzeug.security import generate_password_hash, check_password_hash

from app import db, login


@login.user_loader
def load_user(user_id):
    """Load the user profile.

    Parameters
    ----------
    user_id : str
        user ID.
    """
    return User.query.get(int(user_id))


class User(db.Model):
    """Users table"""
    __tablename__ = 'api_user'

    id = db.Column(db.Integer, primary_key=True)
    public_id = db.Column(db.String(50), unique=True)
    username = db.Column(db.String(50), unique=True)
    password_hash = db.Column(db.String(128))
    is_admin = db.Column(db.Boolean)
    is_active = db.Column(db.Boolean)
    can_debit = db.Column(db.Boolean)
    can_credit = db.Column(db.Boolean)
    mml_username = db.Column(db.String(20), unique=True)
    mml_password = db.Column(db.String(20), unique=True)
    virtual_number = db.Column(db.String(20), unique=True)
    user_type = db.Column(db.String(10))

    def set_password(
            self,
            size=6,
            chars=string.ascii_letters + string.digits):
        """Creates the password hash"""
        random_password = ''.join(random.choice(chars) for i in range(size))
        self.password_hash = generate_password_hash(
            random_password,
            method='sha256'
            )
        return random_password

    def check_password(self, password):
        """Checks if password matches the password hash"""
        return check_password_hash(self.password_hash, password)

    def is_valid(self):
        """Checks if user is valid.
        """
        unique_username = len(
            User.query.filter_by(username=self.username).all()) < 1
        unique_public_id = len(
            User.query.filter_by(public_id=self.public_id).all()) < 1
        unique_mml_username = len(
            User.query.filter_by(mml_username=self.mml_username).all()) < 1
        unique_mml_password = len(
            User.query.filter_by(mml_password=self.mml_password).all()) < 1

        return (
            unique_username and
            unique_public_id and
            unique_mml_username and
            unique_mml_password
            )
