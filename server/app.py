from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_jwt_extended import JWTManager
from flask_cors import CORS
from flasgger import Swagger

import json
from datetime import timedelta


def create_app(db_name, password):
    app = Flask(__name__)
    
    # Application's configuration

    # Postgresql configuration

    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://postgres:{password}@localhost/{db_name}' # authorizing the database
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # JWT tokens configuration

    app.config.from_envvar('ENV_FILE_LOCATION')
    app.config['JWT_TOKEN_LOCATION'] = ['cookies']
    app.config['JWT_COOKIE_SAMESITE'] = 'None'
    app.config['JWT_COOKIE_CSRF_PROTECT'] = False
    app.config['JWT_COOKIE_SECURE'] = True
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(days=1)
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(days=30)

    # Swagger configuration

    app.config['SWAGGER'] = {
        'uiversion': 3,
        'openapi': '3.0.2'
    }

    # Initialize extensions
    # To use the application instances above, instantiate with an application:

    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    jwt.init_app(app)
    cors.init_app(app)
    swagger.init_app(app)

    return app


db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
jwt = JWTManager()
cors = CORS(supports_credentials=True) # CORS configuration to allow including cookies

# Swagger appearance configuration

swagger_config = Swagger.DEFAULT_CONFIG
swagger_config['swagger_ui_bundle_js'] = '//unpkg.com/swagger-ui-dist@3/swagger-ui-bundle.js'
swagger_config['swagger_ui_standalone_preset_js'] = '//unpkg.com/swagger-ui-dist@3/swagger-ui-standalone-preset.js'
swagger_config['jquery_js'] = '//unpkg.com/jquery@2.2.4/dist/jquery.min.js'
swagger_config['swagger_ui_css'] = '//unpkg.com/swagger-ui-dist@3/swagger-ui.css'

swagger = Swagger(template_file='swagger/api_docs.yml', config=swagger_config)

# Setting postgresql login data

with open("local_db_info.json") as ldi:
    info = json.load(ldi)
    db_name = info.get('name')
    password = info.get('password')


app = create_app(db_name, password)