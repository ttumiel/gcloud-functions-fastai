from flask import Flask, escape, jsonify#, request
from utils import generate_text
# app = Flask(__name__)

# @app.route('/', methods=['GET', 'POST'])
def text_endpoint(request):
    """HTTP Cloud Function.
    Args:
        request (flask.Request): The request object.
    Returns:
        The response text.
    """
    request_json = request.get_json(silent=True)
    request_args = request.args

    if request_json and 'data' in request_json:
        data = request_json['data']
    elif request_args and 'data' in request_args:
        data = request_args['data']
        # Get optional parameters here
    else:
        return "Error"
    return jsonify({'text': generate_text(data)})
