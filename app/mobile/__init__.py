from flask import Blueprint

mobile = Blueprint('mobile', __name__)

from . import login, errors, authentication, decorators, api
