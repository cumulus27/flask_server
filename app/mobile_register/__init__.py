from flask import Blueprint

mobile_register = Blueprint('mobile_register', __name__)

from . import register
