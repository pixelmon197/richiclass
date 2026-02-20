from models.user import User
from extensions import db
from werkzeug.security import generate_password_hash
from flask_jwt_extended import create_access_token
from datetime import timedelta
from repository import userRepository

class authService:

    @staticmethod
    def register(username, email, password):
        # Validar si el usuario ya existe
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            return {'error': 'El usuario ya existe'}, 400

        hashed_password = generate_password_hash(password)

        user = User(
            username=username,
            email=email,
            password=hashed_password
        )

        db.session.add(user)
        db.session.commit()

        return user.to_dict(), 201


    @staticmethod
    def get_user_by_id(user_id):
        user = User.query.get(user_id)

        if not user:
            return {'error': 'Usuario no encontrado'}, 404

        return user.to_dict(), 200
    
    @staticmethod
    def login(username,password):
        user = userRepository.get_user_by_user(username)

        if not user:
            return None
        
        check = user.check_password(password)

        claims ={
            "username": user.username
        }

        token = create_access_token(
            identity= str(user.id),
            additional_claims= claims,
            expires_delta= timedelta(hours=8)
        )
        return {
            "access_token": token,
            "user": user
        }