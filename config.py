import os

class Config:
    SECRET_KEY = os.environ.get("SECRET_KEY")
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

class TestConfig(Config): # New class for testing
    TESTING = True # Flask's testing flag
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://remoteroot:remoteroot@localhost:3306/flask_simple_blog_app_test_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:' # In-memory SQLite database
    # For a persistent test database file (useful for debugging test DB state):
    # SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'test.db')
    # You might also want to disable CSRF in testing forms for easier testing:
    WTF_CSRF_ENABLED = False
