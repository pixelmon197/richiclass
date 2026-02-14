from flask import Blueprint, request, jsonify
from services.authService import authService
from flasgger import swag_from

auth_bp = Blueprint('auth', __name__)

# =========================
# REGISTRAR USUARIO
# =========================
@auth_bp.route('/register', methods=['POST'])
@swag_from({
    'tags': ['Users'],
    'consumes': ['application/json'],
    'parameters': [
        {
            'name': 'body',
            'in': 'body',
            'required': True,
            'schema': {
                'type': 'object',
                'properties': {
                    'username': {'type': 'string'},
                    'email': {'type': 'string'},
                    'password': {'type': 'string'}
                },
                'required': ['username', 'email', 'password']
            }
        }
    ],
    'responses': {
        201: {'description': 'Usuario creado'},
        400: {'description': 'Datos inválidos'}
    }
})
def register():
    data = request.get_json()

    # Validación de datos
    if not data or not all(k in data for k in ('username', 'email', 'password')):
        return jsonify({'error': 'Faltan datos obligatorios'}), 400

    result, status = authService.register(
        data['username'],
        data['email'],
        data['password']
    )

    return jsonify(result), status


# =========================
# OBTENER USUARIO POR ID
# =========================
@auth_bp.route('/users/<int:user_id>', methods=['GET'])
@swag_from({
    'tags': ['Users'],
    'parameters': [
        {
            'name': 'user_id',
            'in': 'path',
            'type': 'integer',
            'required': True,
            'description': 'ID del usuario'
        }
    ],
    'responses': {
        200: {'description': 'Usuario encontrado'},
        404: {'description': 'Usuario no encontrado'}
    }
})
def get_user_by_id(user_id):
    result, status = authService.get_user_by_id(user_id)
    return jsonify(result), status
