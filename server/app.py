from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS

import json


def create_app(db_name, password):
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f'postgresql+psycopg2://postgres:{password}@localhost/{db_name}' # authorizing the database (only on localhost now)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Initialize extensions
    # To use the application instances above, instantiate with an application:
    db.init_app(app)
    migrate.init_app(app, db)
    ma.init_app(app)
    cors.init_app(app)

    return app


db = SQLAlchemy()
migrate = Migrate()
ma = Marshmallow()
cors = CORS()

with open("local_db_info.json") as ldi:
    info = json.load(ldi)
    db_name = info.get('name')
    password = info.get('password')

app = create_app(db_name, password)

import auth
# import ...