from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS
from flask_jwt_extended import JWTManager

import json
from datetime import timedelta


def create_app(db_name, password):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://postgres:{password}@localhost/{db_name}' # authorizing the database (only on localhost now)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config.from_envvar('ENV_FILE_LOCATION')
    app.config['JWT_ACCESS_TOKEN_EXPIRES'] = timedelta(seconds=10)
    app.config['JWT_REFRESH_TOKEN_EXPIRES'] = timedelta(minutes=1)

    # Initialize extensions
    # To use the application instances above, instantiate with an application:
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    cors.init_app(app)
    jwt.init_app(app)

    return app


db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
cors = CORS()
jwt = JWTManager()

with open("local_db_info.json") as ldi:
    info = json.load(ldi)
    db_name = info.get('name')
    password = info.get('password')

app = create_app(db_name, password)