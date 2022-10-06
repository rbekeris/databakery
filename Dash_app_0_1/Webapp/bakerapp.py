import os
from Bakerapp import create_app, db
from Bakerapp.User_models import User

bakerapp = create_app(os.getenv("FLASK_CONFIG") or "default")

@bakerapp.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)
