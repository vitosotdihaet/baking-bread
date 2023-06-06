from functools import wraps

from app import app
from api.extensions import db, jwt
from flask import jsonify, request

import requests

import phonenumbers
from phonenumbers import NumberParseException

from flask_jwt_extended import (
    jwt_required, create_access_token,
    create_refresh_token, get_jwt_identity, set_access_cookies,
    set_refresh_cookies, unset_jwt_cookies, verify_jwt_in_request, get_jwt
)

from api.models import User, Admin

from api.error.error_template import ApiError
from api.error.json_validation.auth import AdminLoginAndSignupSchema, UserLoginAndSignupSchema, VerifyOTPSchema, ResendOTPSchema


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



# Only for development, delete for production.
@app.route('/api/user/delete', methods=['GET'])
def delete_users():

    users = User.query.all()
    
    if len(users) == 0 or users == None:
        raise ApiError('NO_USERS_EXIST', status_code=409)

    for user in users:
        db.session.delete(user)

    db.session.commit()

    return 'USERS_DELETED', 200


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


@app.route('/api/user/send_code', methods=['POST'])
def send_verification_code():

    json = request.json
    UserLoginAndSignupSchema().validate(json)

    phone = json.get('phoneNumber')

    try:
        phone = phonenumbers.parse(phone, region='RU')
    except NumberParseException:
        raise ApiError('INVALID_PHONE_NUMBER')

    phone = phonenumbers.format_number(phone, phonenumbers.PhoneNumberFormat.E164)
    phone = phonenumbers.parse(phone, region='RU')

    phone_validaton_1 = phonenumbers.is_valid_number(phone)
    phone_validaton_2 = phonenumbers.is_possible_number(phone)

    if phone_validaton_1 is False or phone_validaton_2 is False:
        raise ApiError('INVALID_PHONE_NUMBER')

    formated_phone = str(phone.country_code) + str(phone.national_number)
    key = 'HkU7Mkp6Yz8OSsumn7SKceut7SMupnaX'
    service = '893091'
    url = 'https://api.ucaller.ru/v1.0/initCall'

    response = requests.get(url + f'?phone={formated_phone}&key={key}&service_id={service}&client={formated_phone}')
    json_response = response.json()

    otp_errors = {
        '3': 'INVALID_PHONE_NUMBER',
        '4': 'OTP_SERVICE_NOT_AVAILABLE',
        '18': 'OTP_REACHED_CALL_LIMIT',
        '19': 'OTP_WAIT_15_SECONDS_LIMIT',
        '429': 'OTP_TOO_MANY_REQUESTS',
        '1001': 'OTP_ACCOUNT_HAS_BEEN_BLOCKED',
        '1002': 'OTP_NOT_ENOUGH_MONEY'
    }

    if json_response['status'] is False:
        if 'error' in json_response:
            status_code = str(json_response['code'])

            if status_code in otp_errors:
                raise ApiError(otp_errors[status_code], 409)

            raise ApiError('OTP_SERVICE_ERROR', 409)
        
        else:
            raise ApiError('OTP_COULD_NOT_CALL', 409)

    uid = str(json_response['ucaller_id'])

    return jsonify(uid=uid), 201


@app.route('/api/user/resend_code', methods=['POST'])
def resend_verification_code():

    json = request.json
    ResendOTPSchema().validate(json)

    uid = json.get('uid')

    key = 'HkU7Mkp6Yz8OSsumn7SKceut7SMupnaX'
    service = '893091'
    url = 'https://api.ucaller.ru/v1.0/initRepeat'

    response = requests.get(url + f'?uid={uid}&key={key}&service_id={service}')
    json_response = response.json()

    otp_errors = {
        '3': 'INVALID_PHONE_NUMBER',
        '4': 'OTP_SERVICE_NOT_AVAILABLE',
        '18': 'OTP_REACHED_CALL_LIMIT',
        '19': 'OTP_WAIT_15_SECONDS_LIMIT',
        '429': 'OTP_TOO_MANY_REQUESTS',
        '1001': 'OTP_ACCOUNT_HAS_BEEN_BLOCKED',
        '1002': 'OTP_NOT_ENOUGH_MONEY'
    }

    if json_response['status'] is False:
        if 'error' in json_response:
            status_code = str(json_response['code'])

            if status_code in otp_errors:
                raise ApiError(otp_errors[status_code], 409)

            raise ApiError('OTP_SERVICE_ERROR', 409)
        
        else:
            raise ApiError('OTP_COULD_NOT_CALL', 409)

    uid = str(json_response['ucaller_id'])

    return jsonify(uid=uid), 201


@app.route('/api/user/verify', methods=['POST'])
def verify_code():

    json = request.json
    VerifyOTPSchema().validate(json)

    uid = str(json.get('uid'))
    code = json.get('code')

    # https://api.ucaller.ru/v1.0/getInfo?uid=103000&key=<Секретный ключ вашего сервиса>&service_id=<Идентификатор сервиса>

    key = 'HkU7Mkp6Yz8OSsumn7SKceut7SMupnaX'
    service = '893091'
    url = 'https://api.ucaller.ru/v1.0/getInfo'

    otp_response = requests.get(url + f'?uid={uid}&key={key}&service_id={service}').json()

    if otp_response['status'] == False:
        if otp_response['code'] == 10:
            raise ApiError('INVALID_OTP_REQUEST_UID')

        raise ApiError('OTP_SERVICE_NOT_AVAILABLE', 409)

    if otp_response['code'] != code:
        raise ApiError('INVALID_OTP_CODE')

    phone = '+' + otp_response['client']

    existing_user = User.query.filter_by(phone=phone).first()

    if existing_user is None:
        new_user = User(phone=phone)

        db.session.add(new_user)
        db.session.commit()

        userId = str(new_user.id)

    else:
        userId = str(existing_user.id)

    access_token = create_access_token(identity=userId, additional_claims={'is_administrator': False})
    refresh_token = create_refresh_token(identity=userId, additional_claims={'is_administrator': False})

    response = jsonify(login=True, adminRights=False, id=userId, background=otp_response)

    # setting access and refresh token in cookies
    set_access_cookies(response, access_token)
    set_refresh_cookies(response, refresh_token)

    return response, 200


@app.route('/api/admin/signup', methods=['POST'])
def signup_admin_post():

    json = request.json
    AdminLoginAndSignupSchema().validate(json)
    username = json.get('username')
    password = json.get('password')

    if username is None or password is None: # check for missing arguments
        raise ApiError('NO_SIGNUP_DATA_PROVIDED')

    user = Admin.query.filter_by(username=username).first()

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
    AdminLoginAndSignupSchema().validate(json)
    username = json.get('username')
    password = json.get('password')


    if username is None or password is None: # check for missing arguments
        raise ApiError('NO_LOGIN_DATA_PROVIDED')

    user = Admin.query.filter_by(username = username).first()

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

    user = User.query.filter_by(id = identity).first()

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

    user = Admin.query.filter_by(id = identity).first()

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

    return jsonify(access='approved', id=identity, adminRights=claims['is_administrator'])


# checks via @admin_required decorator if user has admin rights
@app.route('/api/admin/access', methods=['GET'])
@admin_required()
def admin_protected():

    claims = get_jwt()
    identity = get_jwt_identity()

    return jsonify(access='approved', id=identity, adminRights=claims['is_administrator'])


# # this decorator is mostly used for debugging
# # In that example we print all cookies provided in request before every request
# @app.before_request
# def before_request_func():
#     print(request.cookies)