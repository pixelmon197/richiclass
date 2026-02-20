from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger

db = SQLAlchemy()
migrate = Migrate()

swagger_template = {
    "swagger": "2.0",
    "info": {
        "title": "API",
        "description": "api del 83",
        "version": "1.0"
    },
    "securityDefinitions":{
        "BearerAuth":{
            "type": "apiKey",
            "name": "Authorization",
            "in": "header",
            "description": "Aqui va <token>"
        }
    }
}

Swagger(template=swagger_template)