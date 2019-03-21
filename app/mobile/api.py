from flask import jsonify, request, current_app, url_for
from flask import g
from . import mobile


@mobile.route('/test/')
def connect_test():
    response = {}
    response.update({"state": "Success login"})
    response.update({"message": "You are success login, {}".format(g.current_user.username)})
    response.update({"data": ""})

    return jsonify(response)
