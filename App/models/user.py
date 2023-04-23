from werkzeug.security import check_password_hash, generate_password_hash
from flask_login import UserMixin
from App.database import db

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username =  db.Column(db.String, nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(120), nullable=False)

    def __init__(self, username, password):
        self.username = username
        self.set_password(password)

    def get_json(self):
        return{
            'id': self.id,
            'username': self.username
        }

    def set_password(self, password):
        """Create hashed password."""
        self.password = generate_password_hash(password, method='sha256')
    
    def check_password(self, password):
        """Check hashed password."""
        return check_password_hash(self.password, password)

class RegularUser(User):
    __tablename__ = 'regular_user'
    competitions = db.relationship(
    'Competitions', secondary='user_competition',
                          backref=db.backref('regular_users', lazy=True))  # sets up a relationship to competitions which references Regular
    
class Competitions(db.Model):
    __tablename__ = 'competitions'
    id = db.Column(db.Integer, primary_key=True)
    details = db.Column(db.String(1000), nullable=False)
    reg_open = db.Column(db.Boolean, default=False)
    comp_ended = db.Column(db.Boolean, default=False)

    def view_comp_details(): 

class Results(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    admin_id = db.Column(db.Integer, db.ForeignKey('admin.id'), nullable=False)
    competition_id = db.Column(db.Integer, db.ForeignKey('competitions.id') nullable=False)

    def view_results():

