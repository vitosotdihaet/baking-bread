from app import app
from api.extensions import jwt
from flask import jsonify
from api.error.error_template import ApiError

@app.errorhandler(ApiError) # handles all kinds of custom errors (executes with `raise ApiError({some data})`)
def error_response_callback(error):
    return jsonify(error.to_dict()), error.status_code


@app.errorhandler(405)
def error_response_callback(error):
    return jsonify(message='METHOD_NOT_ALLOWED'), 405


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