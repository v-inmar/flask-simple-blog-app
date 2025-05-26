from flask import Flask
from config import Config

from app.extensions import db, login_manager, migrate


def create_app(config_class=Config):
    app = Flask(import_name=__name__, instance_relative_config=True) # will enable instance directory to load config file, if there is any
    app.config.from_object(config_class)
    app.template_folder="templates" # global templates folder - holds base.html

    db.init_app(app=app)
    migrate.init_app(app=app, db=db)
    login_manager.init_app(app=app)


    # Utility function for Flask-Login for managing user sessions
    from app.utils import user_loader

    # Load custom error handlers
    from app.errors import load_errors
    load_errors(app=app)

    # -- Load the modules -- #
    from app.modules import load_modules
    load_modules(app=app)

    return app