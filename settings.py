from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'this-really-needs-to-be-changed'
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']

class ProductionConfig(Config):
    DEBUG = False

class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True

class TestingConfig(Config):
    TESTING = True

# # Shared app instance
# app = Flask(__name__)

# # PORT
# PORT = os.getenv(PORT, 5000)

# # Set debug mode
# app.config['DEBUG'] = os.getenv(DEBUG, False)

# # configuration
# app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv(DATABASE_URL, "")
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = os.getenv(TRACK_MODIFICATIONS, False)

# # Create DB instance
# db = SQLAlchemy(app)