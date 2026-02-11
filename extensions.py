from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flasgger import Swagger

db = SQLAlchemy()
migrate = Migrate()

Swagger_template= {
    'swagger': "2.0",
    "info":{
        "title": "API",
        "description": "api del 83",
        "version": "1.0"
    }
}
Swagger = Swagger(template= Swagger_template)