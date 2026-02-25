from flask import Blueprint, jsonify
from   flask_jwt_extended import jwt_required,get_jwt_identity,get_jwt
from flasgger import swag_from

user_bp = Blueprint('users', __name__)

@user_bp.route('/me')
@jwt_required()
@swag_from({
    "tags": ["Users"],
    "security":[{"BearerAuth": []}],
    "responses":{
        200: {
            "description": "Informacion del usuario autentificado",
            "examples":{
                "application/json":{
                    "id": "2",
                    "username": "richie2050"
                }
            }
        },
        401: {
            "description": "token invalido o ausente"
        }
    }
})

def me ():
    user_id = get_jwt_identity()
    claims = get_jwt()
    return jsonify({
        "id": user_bp,
        "username": claims.get('username')
    }),200