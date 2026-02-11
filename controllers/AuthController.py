from flask import Blueprint, request, jsonify
from services.authService import authService
from flasgger import swag_from

auth_bp = Blueprint('auth', __name__)

@auth_bp.route('/register', methods=['GET', 'POST'])
@swag_from({
    'tags':["Users"],
    'parameters':[{
        'name': 'body',
         'schema':{
             'type': 'object',
             'property':{
                 'username':{'type': 'sting'},
                 'email':{'type': 'sting'},
                 'password':{'type': 'sting'}
             },
            'required': ['username','email','password']
         }   
        }
    ],
    'responses':{
        200:{
            'description':'Usuario creado'
        }
    }
})
def register():
    if request.method == 'GET':
        return jsonify({'message': 'Auth route working'}), 200

    data = request.get_json()
    try:
        user = authService.register(data['username'], data['email'], data['password'])
        print('User',user)
        return jsonify(user.to_dict()), 201
    except ValueError as e:
        print(e)
        return jsonify({'mensage': e}),500
    
@auth_bp.route('/users/<int:id>', methods=['GET'])
def find_by_id(id):
    try:
        user= authService.find_by_id(id)
        print('USER',user)
        return jsonify(user.to_dict()),201
    
    except ValueError as e:
        print(e)
        return jsonify({'mensaje': str(e)}),500