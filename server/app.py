from flask import Flask
from api.extensions import db, migrate, ma, jwt, cors, swagger
from configs.app_config import Staging

# import flask_monitoringdashboard as dashboard
# from flask_jwt_extended import get_jwt_identity, verify_jwt_in_request


def create_app():
    app = Flask(__name__)
    
    # Application's configuration

    app.config.from_object(Staging())
    app.config.from_envvar('ENV_FILE_LOCATION')

    # Monitoring dashboard configuration

    # def get_user_id():
    #     try:
    #         verify_jwt_in_request()
    #     except:
    #         return 'anonimous client'

    #     return get_jwt_identity()


    # dashboard.config.group_by = get_user_id
    # dashboard.config.init_from(file='configs/dashboard.cfg')
    # dashboard.bind(app)


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
app = create_app()