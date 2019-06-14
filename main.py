from flask import Flask, escape, jsonify
from utils import generate_text, classify_text
import random

from config import DEFAULT_WORDS

def endpoint(func):
    def wrapper(request):
        request_json = request.get_json(silent=True)
        request_args = request.args

        if request_json and 'data' in request_json:
            args = request_json
        elif request_args and 'data' in request_args:
            args = request_args
        else:
            args = {"data":random.choice(DEFAULT_WORDS)}
        
        try:
            resp = func(**args)
        except:
            resp = {}

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
