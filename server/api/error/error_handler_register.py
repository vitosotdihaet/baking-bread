from app import app
from api.error.error_template import ApiError


@app.errorhandler(ApiError) # handles all kinds of custom errors (executes with `raise ApiError({some data})`)
def error_response_callback(error):
    return jsonify(error.to_dict()), error.status_code


@app.errorhandler(405)
def error_response_callback(error):
    return jsonify(message='METHOD_NOT_ALLOWED'), 405