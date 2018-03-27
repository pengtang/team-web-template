# Define user class
from flask_login import UserMixin
from project.extensions import bcrypt, db


class RegisteredUser(UserMixin, db.Model):

    __tablename__ = "registered_user"

    id = db.Column(db.BigInteger, primary_key=True, unique=True, nullable=False)
    username = db.Column(db.Text, unique=True, nullable=False)
    password = db.Column(db.Binary(60), nullable=False)
    email = db.Column(db.Text, unique=True, nullable=False)

    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = bcrypt.generate_password_hash(password)
        self.email = email

    def set_password(self, password):
        """Set password."""
        self.password = bcrypt.generate_password_hash(password)

    def check_password(self, value):
        """Check password."""
        return bcrypt.check_password_hash(self.password, value)

    def __repr__(self):
        return '<User %r>' % self.username


# Define team_member class
