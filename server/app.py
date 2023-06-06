from flask import Flask
from api.extensions import db, migrate, ma, jwt, cors, swagger
from configs.constants import cfg

import flask_monitoringdashboard as dashboard
from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request

import json
from datetime import timedelta


def create_app(db_name, password):
    app = Flask(__name__)
    
    # Application's configuration

    # Monitoring dashboard configuration

    def get_user_id():
        try:
            verify_jwt_in_request()
        except:
            return 'anonimous client'

        return get_jwt_identity()


    dashboard.config.group_by = get_user_id
    dashboard.config.init_from(file='configs/dashboard.cfg')
    dashboard.bind(app)

    # Postgresql configuration

    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://postgres:{password}@localhost/{db_name}' # authorizing the database (only on localhost now)
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


# Create Flask application
app = create_app(cfg['postgres']['DB_NAME'], cfg['postgres']['DB_PASSWORD'])