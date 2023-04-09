from app import app
from flask import request

# import markdown
# import markdown.extensions.fenced_code
# from pygments.formatters import HtmlFormatter

# all users have access to this endpont (no access token required)
@app.route('/api', methods=['POST'])
def test():
    return request.files['file'].read() # response with a file from a request containing form-data with this file