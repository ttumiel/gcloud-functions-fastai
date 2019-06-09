"Helps testing functions that you want to deploy."
from flask import Flask
app = Flask(__name__)


class DummyRequest():
    def __init__(self, json_data, query_str_data):
        self.json_data = json_data
        self.args = query_str_data

    def get_json(self, **kwargs):
        return self.json_data

def test_function(func, json_data=None, query_str_data=None):
    req = DummyRequest(json_data, query_str_data)
    with app.app_context():
        return func(req).get_json()
