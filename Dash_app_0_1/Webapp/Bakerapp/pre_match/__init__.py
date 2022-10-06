from flask import Blueprint

pre_match = Blueprint('pre_match', __name__)

from . import views
