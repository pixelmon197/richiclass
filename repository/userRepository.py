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
