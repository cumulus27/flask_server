
"""
    Flask server.
    export FLASK_APP=server.py
    flask run
"""

from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/v1/test')
def connect_test():
    response = {}
    response.update({"code": 200})
    response.update({"message": "Connect test pass"})
    response.update({"data": ""})

    return jsonify(response)
