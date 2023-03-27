from functools import wraps

from app import db, app, jwt
from flask import abort, jsonify, request, redirect, url_for
from flask_jwt_extended import create_access_token, jwt_required, get_jwt_identity, create_refresh_token, get_jwt, verify_jwt_in_request
from sqlalchemy.exc import IntegrityError
from models import User


class InvalidApi(Exception): # editable class template for all kinds of errors
    status_code = 400 # default status code, if it's not provided


    def __init__(self, error, status_code=None):
        super().__init__

        self.error = error

        if status_code is not None:
            self.status_code = status_code


    def to_dict(self):
        for_json = dict()
        for_json['Message'] = self.error
        
        return for_json


@app.errorhandler(InvalidApi) # errorhandler for @app.routes for all kinds of errors (executes with 'raise InvalidApi({some data})')
def error_response_callback(error):
    return jsonify(error.to_dict()), error.status_code


@jwt.invalid_token_loader
def invalid_token_callback(error_string):
    return jsonify(Error='INVALID_TOKEN'), 422


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify(Error='TOKEN_HAS_EXPIRED'), 401


@jwt.unauthorized_loader
def unauthorized_callback(error_string):
    return jsonify(Error='NO_TOKEN_PROVIDED'), 401


@jwt.needs_fresh_token_loader
def no_fresh_token_callback(jwt_header, jwt_payload):
    return jsonify(Error='NO_FRESH_TOKEN_PROVIDED'), 401


# Here is a custom decorator that verifies the token is present in the request,
# as well as insuring that the tpken has a claim indicating that this user is
# an administrator
def admin_required():
    def wrapper(fn):

        @wraps(fn)
        def decorator(*args, **kwargs):
            verify_jwt_in_request()
            claims = get_jwt()

            if claims["is_administrator"]:
                return fn(*args, **kwargs)
            else:
                return jsonify(Error='ADMIN_RIGHTS_REQUIRED'), 403

        return decorator

    return wrapper


@app.route('/signup', methods=['POST'])
def signup_post():
    username = request.json.get('username')
    password = request.json.get('password')

    if username is None or password is None: # check for missing arguments
        raise InvalidApi('LACK_OF_SINGUP_DATA')

    user = User(username=username)
    user.hash_password(password)

    try: # check if user already exists
        db.session.add(user)
        db.session.commit()
    except IntegrityError:
        db.session.rollback()
        raise InvalidApi('USER_ALREADY_EXISTS', status_code=409)

    return "something in return"


@app.route('/login', methods=['POST'])
def login_post():
    username = request.json.get('username')
    password = request.json.get('password')

    if username is None or password is None: # check for missing arguments
        raise InvalidApi('LACK_OF_LOGIN_DATA')

    user = db.session.query(User).filter_by(username = username).first()

    if user is None:
        raise InvalidApi('INVALID_LOGIN')

    authorized = user.verify_password(password)

    if not authorized:
        raise InvalidApi('INVALID_PASSWORD')

    str_user_id = str(user.id)

    # creating access token with info of user id and admin rights and refresh token with info of user id
    access_token = create_access_token(identity=str_user_id, additional_claims={"is_administrator": False})
    refresh_token = create_refresh_token(identity=str_user_id)

    return jsonify(access_token=access_token, refresh_token=refresh_token)


# We are using the `refresh=True` options in jwt_required to only allow
# refresh tokens to access this route.
@app.route("/refresh", methods=["POST"])
@jwt_required(refresh=True)
def refresh():
    identity = get_jwt_identity() # getting id of our user from token

    access_token = create_access_token(identity=identity, additional_claims={"is_administrator": False})

    return jsonify(access_token=access_token)


# checks via @jwt_required decorator if user has logged in 
@app.route("/user-access", methods=["GET"])
@jwt_required()
def user_protected():
    return jsonify(Access='approved')


# checks via @admin_required decorator if user has admin rights
@app.route("/admin-access", methods=["GET"])
@admin_required()
def admin_protected():
    return jsonify(Access='approved')