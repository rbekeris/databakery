from flask import Flask, render_template
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config
from flask import url_for
from wtforms import ValidationError, fields
from wtforms.widgets import html_params
from markupsafe import Markup
from gettext import gettext
from flask import Flask
import json


bootstrap = Bootstrap()
moment = Moment()
db = SQLAlchemy()

login_manager = LoginManager()
"""The login_view attribute of the LoginManager object sets the endpoint for the login page.
Flask-Login will redirect to the login page when an anonymous user tries to access a protected page.
Because the login route is inside a blueprint, it needs to be
prefixed with the blueprint name."""
login_manager.login_view = "auth.login"


def create_app(config_name):
    """application factory"""
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)
    moment.init_app(app)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    from .post_match import post_match as post_match_blueprint
    app.register_blueprint(post_match_blueprint, url_prefix="/post_match")

    from .pre_match import pre_match as pre_match_blueprint
    app.register_blueprint(pre_match_blueprint, url_prefix="/pre_match")

    from .User_models import (
        User
    )

    from .Game_models import (
        Heroes,
        Items
    )
    return app
