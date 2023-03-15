from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_marshmallow import Marshmallow
from flask_cors import CORS

db = SQLAlchemy()
migrate = Migrate()
msh = Marshmallow()
cors = CORS()

def createApp():
  app = Flask(__name__)
  
  # database connecting (only on localhost yet)
  app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql+psycopg2://postgres:test3915@localhost/bakingBread"
  app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
  
  db.init_app(app)
  migrate.init_app(app, db)
  msh.init_app(app)
  cors.init_app(app)
  
  return app