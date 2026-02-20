from extensions import db
from models.user import User

class UserRepository:
    @staticmethod
    def create(username,email,password):
        user = User(
            username = username,
            email= email
        )
        user.set_password(password)
        db.session.add(user)
        db.session.commit()
        return user

@staticmethod
def find_by_user(username):
    return User.query.filter_by(username=username).first()

@staticmethod
def find_by_email(email):
    return User.query.filter_by(email=email).first()