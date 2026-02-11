from flask import Blueprint

blueprint_home = Blueprint('home', __name__)
@blueprint_home.route('/home')
def home():
    return {'msn' : 'hola desde home'}