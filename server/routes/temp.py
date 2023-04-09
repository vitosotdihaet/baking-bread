from app import app
from flask import request, jsonify


# all users have access to this endpont (no access token required)
@app.route('/', methods=['GET'])
def test():
    return jsonify(Hello='world')


# all users have access to this endpont (no access token required)
@app.route('/api', methods=['POST'])
def test_form_data_file():
    return request.files['file'].read() # response with a file from a request containing form-data with this file