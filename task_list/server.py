"""
    Flask server.
    export FLASK_APP=server.py
    flask run
"""

from flask import Flask
from flask import jsonify

from flask import (
    Blueprint, flash, redirect, render_template, request, url_for
)

from task_list import db
from task_list.models import Task

app = Blueprint('task_list', __name__)


@app.route('/v1/test')
def connect_test():
    response = {}
    response.update({"code": 200})
    response.update({"message": "Connect test pass"})
    response.update({"data": ""})

    return jsonify(response)
