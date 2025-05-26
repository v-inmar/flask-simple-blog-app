# Contains initialization of extensions/packages used
# This can help avoid circular imports
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager

db = SQLAlchemy()
migrate = Migrate()
login_manager = LoginManager()

# Set the login view for Flask-Login
login_manager.login_view = 'auth.login' # This tells login manager where to redirect if login is required
login_manager.login_message_category = 'info' # Category for flash messages