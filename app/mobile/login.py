from flask import g, jsonify
from flask_httpauth import HTTPBasicAuth
from ..models import User
from . import mobile
from .errors import unauthorized, forbidden

auth = HTTPBasicAuth()


@mobile.route('/login/', methods=['POST'])
def mobile_login():
    if g.current_user.is_anonymous or g.token_used:
        return unauthorized('Invalid credentials')
    return jsonify({'token': g.current_user.generate_auth_token(
        expiration=360000), 'expiration': 360000})
