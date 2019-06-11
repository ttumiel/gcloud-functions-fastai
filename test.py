"Helps test functions that you want to deploy."
from flask import Flask

class DummyRequest():
    def __init__(self, json_data, query_str_data):
        self.json_data = json_data
        self.args = query_str_data

    def get_json(self, *args, **kwargs):
        return self.json_data

def test_function(func, json_data=None, query_str_data=None):
    app = Flask(__name__)
    req = DummyRequest(json_data, query_str_data)
    with app.app_context():
        return func(req).get_json()
