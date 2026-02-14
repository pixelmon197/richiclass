from models.user import User
from extensions import db
from werkzeug.security import generate_password_hash

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
