from flask import Flask
from controllers.HomeController import blueprint_home
from extensions import db, migrate
from config import Config
from controllers.AuthController import auth_bp
from flasgger import Swagger


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    Swagger(app)

    app.register_blueprint(auth_bp, url_prefix='/api/auth')
    app.register_blueprint(blueprint_home)

    @app.route('/')
    def home():
        return {'mensaje': 'hola mundo'}, 200

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5001)
