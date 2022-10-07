from flask import render_template
from . import pre_match
@pre_match.route('/')
def index():
    return render_template('second.html')