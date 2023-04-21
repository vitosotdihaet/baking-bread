from functools import wraps

from app import db, app, jwt
from flask import abort, jsonify, request, redirect, url_for

from flask_jwt_extended import (
    jwt_required, create_access_token,
    create_refresh_token, get_jwt_identity, set_access_cookies,
    set_refresh_cookies, unset_jwt_cookies, verify_jwt_in_request, get_jwt
)

from models import User, Admin
from api_calls.error import ApiError
from api_calls.json_validation import LoginAndSignupSchema


# ERROR HANDLING PART

@jwt.invalid_token_loader
def invalid_token_callback(error_string):
    return jsonify(message='INVALID_TOKEN'), 422


@jwt.expired_token_loader
def expired_token_callback(jwt_header, jwt_payload):
    return jsonify(message='TOKEN_HAS_EXPIRED'), 401


@jwt.unauthorized_loader
def unauthorized_callback(error_string):
    return jsonify(message='NO_TOKEN_PROVIDED'), 401


@jwt.needs_fresh_token_loader
def no_fresh_token_callback(jwt_header, jwt_payload):
    return jsonify(message='NO_FRESH_TOKEN_PROVIDED'), 401


# AUTHENTICATION PART

# A custom decorator that verifies that token is present in the request,
# as well as insuring that the token has a claim indicating that the user is
# an administrator
def admin_required():
    def wrapper(fn):

        @wraps(fn)
        def decorator(*args, **kwargs):

            verify_jwt_in_request()
            claims = get_jwt()

            if claims['is_administrator']:
                return fn(*args, **kwargs)

            return jsonify(message='ADMIN_RIGHTS_REQUIRED'), 403

        return decorator

    return wrapper


@app.route('/api/user/signup', methods=['POST'])
def signup_post():

    json = request.json
    LoginAndSignupSchema().validate(json)
    username = json.get('username')
    password = json.get('password')

    user = db.session.query(User).filter_by(username=username).first()

    if user is not None:
        raise ApiError('USER_ALREADY_EXISTS', status_code=409)


    user = User(username=username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()

    userId = str(user.id)

    # creating access token with info of user id and admin rights and refresh token with info of user id
    # note that here we set `fresh=True` for access to endpoint `delete-account`
    # [DEPRECATED UNTIL PRODUCTION] User will have `fresh=False` parameter in token with accessing `signup` endpoint and `refresh` endpoint
    # so anyone who has fresh token could not do some crtitical things without fresh token, such as deleting an account
    access_token = create_access_token(identity=userId, additional_claims={'is_administrator': False})
    refresh_token = create_refresh_token(identity=userId, additional_claims={'is_administrator': False})

    response = jsonify(login=True, adminRights=False, id=userId)

    # setting access and refresh token in cookies
    set_access_cookies(response, access_token)
    set_refresh_cookies(response, refresh_token)

    return response, 201


@app.route('/api/user/login', methods=['POST'])
def login_post():

    json = request.json
    LoginAndSignupSchema().validate(json)
    username = json.get('username')
    password = json.get('password')


    if username is None or password is None: # check for missing arguments
        raise ApiError('NO_LOGIN_DATA_PROVIDED')

    user = db.session.query(User).filter_by(username = username).first()

    if user is None:
        raise ApiError('INVALID_LOGIN_OR_PASSWORD', status_code=409)

    authorized = user.verify_password(password)

    if not authorized:
        raise ApiError('INVALID_LOGIN_OR_PASSWORD', status_code=409)


    userId = str(user.id)

    # creating access token with info of user id and admin rights and refresh token with info of user id
    access_token = create_access_token(identity=userId, additional_claims={'is_administrator': False})
    refresh_token = create_refresh_token(identity=userId, additional_claims={'is_administrator': False})

    response = jsonify(login=True, adminRights=False, id=userId)

    # setting access and refresh token in cookies
    set_access_cookies(response, access_token)
    set_refresh_cookies(response, refresh_token)

    return response, 201


@app.route('/api/admin/signup', methods=['POST'])
def signup_admin_post():

    json = request.json
    LoginAndSignupSchema().validate(json)
    username = json.get('username')
    password = json.get('password')

    if username is None or password is None: # check for missing arguments
        raise ApiError('NO_SIGNUP_DATA_PROVIDED')

    user = db.session.query(Admin).filter_by(username=username).first()

    if user is not None:
        raise ApiError('ADMIN_ALREADY_EXISTS', status_code=409)


    user = Admin(username=username)
    user.hash_password(password)
    db.session.add(user)
    db.session.commit()

    userId = str(user.id)

    # creating access token with info of user id and admin rights and refresh token with info of user id
    # note that here we set `fresh=True` for access to endpoint `delete-account`
    # [DEPRECATED UNTIL PRODUCTION] User will have `fresh=False` parameter in token with accessing `signup` endpoint and `refresh` endpoint
    # so anyone who has fresh token could not do some crtitical things without fresh token, such as deleting an account
    access_token = create_access_token(identity=userId, additional_claims={'is_administrator': True})
    refresh_token = create_refresh_token(identity=userId, additional_claims={'is_administrator': True})

    response = jsonify(login=True, adminRights=True, id=userId)

    # setting access and refresh token in cookies
    set_access_cookies(response, access_token)
    set_refresh_cookies(response, refresh_token)

    return response, 201


@app.route('/api/admin/login', methods=['POST'])
def login_admin_post():

    json = request.json
    LoginAndSignupSchema().validate(json)
    username = json.get('username')
    password = json.get('password')


    if username is None or password is None: # check for missing arguments
        raise ApiError('NO_LOGIN_DATA_PROVIDED')

    user = db.session.query(Admin).filter_by(username = username).first()

    if user is None:
        raise ApiError('INVALID_LOGIN_OR_PASSWORD', status_code=409)

    authorized = user.verify_password(password)

    if not authorized:
        raise ApiError('INVALID_LOGIN_OR_PASSWORD', status_code=409)


    userId = str(user.id)

    # creating access token with info of user id and admin rights and refresh token with info of user id
    access_token = create_access_token(identity=userId, additional_claims={'is_administrator': True})
    refresh_token = create_refresh_token(identity=userId, additional_claims={'is_administrator': True})

    response = jsonify(login=True, adminRights=True, id=userId)

    # setting access and refresh token in cookies
    set_access_cookies(response, access_token)
    set_refresh_cookies(response, refresh_token)

    return response, 201


# checks via @jwt_required decorator if user has access-token
@app.route('/api/logout', methods=['POST'])
@jwt_required()
def logout_post():

    response = jsonify(logout=True)

    unset_jwt_cookies(response)

    return response


# checks via @jwt_required decorator if user has access-token
@app.route('/api/user', methods=['DELETE'])
@jwt_required()
def delete_user():

    claims = get_jwt()
    identity = get_jwt_identity()

    if claims['is_administrator']:
        raise ApiError('ONLY_FOR_USERS', 403)

    user = db.session.query(User).filter_by(id = identity).first()

    if user is None:
        raise ApiError('USER_DOESNT_EXIST', 409)

    db.session.delete(user)
    db.session.commit()

    response = jsonify(deleted_account=True, id=identity)
    unset_jwt_cookies(response)

    return response


# checks via @admin_required decorator if user has admin rights
@app.route('/api/admin', methods=['DELETE'])
@admin_required()
def delete_admin():

    identity = get_jwt_identity()

    user = db.session.query(Admin).filter_by(id = identity).first()

    if user is None:
        raise ApiError('ADMIN_DOESNT_EXIST', 409)

    db.session.delete(user)
    db.session.commit()

    response = jsonify(deletedAdmin=True, id=identity)
    unset_jwt_cookies(response)

    return response


# We are using the `refresh=True` options in jwt_required to only allow
# refresh tokens to access this route.
@app.route('/api/refresh', methods=['POST'])
@jwt_required(refresh=True)
def refresh_token():

    claims = get_jwt()
    identity = get_jwt_identity() # getting id of our user from the token
    adminRights = claims['is_administrator']

    access_token = create_access_token(identity=identity, additional_claims={'is_administrator': adminRights})

    response = jsonify(refresh=True)
    set_access_cookies(response, access_token)

    return response


# checks via @jwt_required decorator if user has access-token
@app.route('/api/user/access', methods=['GET'])
@jwt_required()
def user_protected():

    claims = get_jwt()
    identity = get_jwt_identity()

    return jsonify(Access='approved', id=identity, adminRights=claims['is_administrator'])


# checks via @admin_required decorator if user has admin rights
@app.route('/api/admin/access', methods=['GET'])
@admin_required()
def admin_protected():

    claims = get_jwt()
    identity = get_jwt_identity()

    return jsonify(Access='approved', id=identity, adminRights=claims['is_administrator'])


# # this decorator is mostly used for debugging
# # In that example we print all cookies provided in request before every request
# @app.before_request
# def before_request_func():
#     print(request.cookies)