from app import app
from flask import jsonify


class ApiError(Exception): # editable class template for all kinds of errors
    status_code = 400 # default status code 'BAD_REQUEST', if it's not provided


    def __init__(self, error, status_code=None):
        super().__init__

        self.error = error

        if status_code is not None:
            self.status_code = status_code


    def to_dict(self): # returning json response with a name of an error
        for_json = dict()
        for_json['Message'] = self.error
        
        return for_json

@app.errorhandler(ApiError) # handles all kinds of errors (executes with `raise ApiError({some data})`)
def error_response_callback(error):
    return jsonify(error.to_dict()), error.status_code
