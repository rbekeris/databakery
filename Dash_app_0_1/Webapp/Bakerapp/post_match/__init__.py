from flask import Blueprint

post_match = Blueprint('post_match', __name__)

from . import views
