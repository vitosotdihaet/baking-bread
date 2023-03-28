from app import app
from flask import jsonify

# all users have access to this endpont (no access token required)
@app.route('/', methods=['GET'])
def test():
    return jsonify(Hello='world')
