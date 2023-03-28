from functools import wraps

from app import db, app, jwt
from flask import abort, jsonify, request, redirect, url_for
from flask_jwt_extended import (
    jwt_required, create_access_token,
    create_refresh_token, get_jwt_identity, set_access_cookies,
    set_refresh_cookies, unset_jwt_cookies, verify_jwt_in_request, get_jwt
)
from sqlalchemy.exc import IntegrityError
from models import User

from api_calls.error import ApiError


# ERROR HANDLING PART

@app.errorhandler(ApiError) # errorhandler for @app.routes for all kinds of errors (executes with `raise ApiError({some data})`)
def error_response_callback(error):
    return jsonify(error.to_dict()), error.status_code


@jwt.invalid_token_loader
def invalid_token_callback(error_string):
    return jsonify(Message='INVALID_TOKEN'), 422


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify(Message='TOKEN_HAS_EXPIRED'), 401


@jwt.unauthorized_loader
def unauthorized_callback(error_string):
    return jsonify(Message='NO_TOKEN_PROVIDED'), 401


@jwt.needs_fresh_token_loader
def no_fresh_token_callback(jwt_header, jwt_payload):
    return jsonify(Message='NO_FRESH_TOKEN_PROVIDED'), 401


# AUTHENTIFICATION PART

# Here is a custom decorator that verifies the token is present in the request,
# as well as insuring that the token has a claim indicating that this user is
# an administrator
def admin_required():
    def wrapper(fn):

        @wraps(fn)
        def decorator(*args, **kwargs):

            verify_jwt_in_request()
            claims = get_jwt()

            if claims['is_administrator']:
                return fn(*args, **kwargs)
            else:
                return jsonify(Error='ADMIN_RIGHTS_REQUIRED'), 403

        return decorator

    return wrapper


@app.route('/api/signup', methods=['POST'])
def signup_post():

    username = request.json.get('username')
    password = request.json.get('password')

    if username is None or password is None: # check for missing arguments
        raise ApiError('LACK_OF_SINGUP_DATA')

    user = db.session.query(User).filter_by(username=username).first()

    if user is not None:
        raise ApiError('USER_ALREADY_EXISTS', status_code=409)


    user = User(username=username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()

    userId = str(user.id)

    response = jsonify(signup=True)

    # creating access token with info of user id and admin rights and refresh token with info of user id
    # note that here we set `fresh=True` for access to endpoint `delete-account`
    # User will have `fresh=False` parameter in token with accessing `signup` endpoint and `refresh` endpoint
    # so anyone who has fresh token could not do some crtitical things without fresh token, such as deleting an account
    access_token = create_access_token(identity=userId, additional_claims={'is_administrator': False}, fresh=False)
    refresh_token = create_refresh_token(identity=userId)

    # setting access and refresh token in cookies
    set_access_cookies(response, access_token)
    set_refresh_cookies(response, refresh_token)

    return response


@app.route('/api/login', methods=['POST'])
def login_post():

    username = request.json.get('username')
    password = request.json.get('password')


    if username is None or password is None: # check for missing arguments
        raise ApiError('LACK_OF_LOGIN_DATA')

    user = db.session.query(User).filter_by(username = username).first()

    if user is None:
        raise ApiError('INVALID_LOGIN_OR_PASSWORD')

    authorized = user.verify_password(password)

    if not authorized:
        raise ApiError('INVALID_LOGIN_OR_PASSWORD')


    userId = str(user.id)

    response = jsonify(login=True)

    # creating access token with info of user id and admin rights and refresh token with info of user id
    access_token = create_access_token(identity=userId, additional_claims={'is_administrator': False}, fresh=True)
    refresh_token = create_refresh_token(identity=userId)

    # setting access and refresh token in cookies
    set_access_cookies(response, access_token)
    set_refresh_cookies(response, refresh_token)

    return response


@app.route('/api/logout', methods=['POST'])
def logout_post():

    response = jsonify({'logout': True})

    unset_jwt_cookies(response)

    return response


@app.route('/api/delete-account', methods=['DELETE'])
@jwt_required(fresh=True)
def delete_account():

    identity = get_jwt_identity()

    user = db.session.query(User).filter_by(id = identity).first()

    if user is None:
        raise ApiError('USER_DOESNT_EXIST')

    db.session.delete(user)
    db.session.commit()

    response = jsonify({'deleted_account': True})
    unset_jwt_cookies(response)

    return response


# We are using the `refresh=True` options in jwt_required to only allow
# refresh tokens to access this route.
@app.route('/api/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh_token():

    identity = get_jwt_identity() # getting id of our user from token
    access_token = create_access_token(identity=identity, additional_claims={'is_administrator': False}, fresh=False)

    response = jsonify({'refresh': True})
    set_access_cookies(response, access_token)

    return response


# checks via @jwt_required decorator if user has access-token
@app.route('/api/user-access', methods=['GET'])
@jwt_required()
def user_protected():

    identity = get_jwt_identity()

    return jsonify(Access='approved', Identity=identity)


# checks via @admin_required decorator if user has admin rights
@app.route('/api/admin-access', methods=['GET'])
@admin_required()
def admin_protected():

    identity = get_jwt_identity()

    return jsonify(Access='approved', Identity=identity)


# all users have access to this endpont (no access token required)
@app.route('/', methods=['GET'])
def test():
    return jsonify(Hello='world')


# # this decorator is mostly used for debugging
# # In that example we print all cookies provided in request before every request
# @app.before_request
# def before_request_func():
#     print(request.cookies)