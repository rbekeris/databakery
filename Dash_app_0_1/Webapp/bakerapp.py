import os
from Bakerapp import create_app, db
from Bakerapp.User_models import User
from flask_migrate import Migrate

bakerapp = create_app(os.getenv("FLASK_CONFIG") or "default")
migrate = Migrate(bakerapp, db)


@bakerapp.shell_context_processor
def make_shell_context():
    return dict(db=db, User=User)
