from flask import Flask, escape, jsonify#, request
from utils import generate_text, classify_text
import random

from config import DEFAULT_WORDS
# app = Flask(__name__)

def endpoint(func):
    def wrapper(request):
        request_json = request.get_json(silent=True)
        request_args = request.args

        if request_json and 'data' in request_json:
            data = request_json['data']
        elif request_args and 'data' in request_args:
            data = request_args['data']
            # Get optional parameters here
        else:
            data = random.choice(DEFAULT_WORDS)
        
        resp = func(data)
        return jsonify(resp)
    return wrapper

# @app.route('/', methods=['GET', 'POST'])
@endpoint
def text_gen(data):
    "Text generation cloud function."
    return {'text': generate_text(data)}

@endpoint
def text_clas(data):
    "Text classification cloud function."
    return classify_text(data)
