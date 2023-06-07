from flask import jsonify
from flask_jwt_extended import verify_jwt_in_request, get_jwt
from functools import wraps


# A custom decorator that verifies that token is present in the request,
# as well as insuring that the token has a claim indicating that the user has
# an appropriate role
def role_required(role):
    def wrapper(fn):

        @wraps(fn)
        def decorator(*args, **kwargs):

            verify_jwt_in_request()
            claims = get_jwt()

            if claims[role]:
                return fn(*args, **kwargs)

            return jsonify(message=f'{role.upper()}_RIGHTS_REQUIRED'), 403

        return decorator

    return wrapper