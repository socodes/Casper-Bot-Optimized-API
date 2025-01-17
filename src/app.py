from flask import Flask
from src.api import api
from src.errors import errors
from dotenv import load_dotenv
from src.factory import database
from src.config import *

"""
Create flask application and make necessary adjustments. Load environment, configure flask application settings, initiliaze database connection
"""

def create_app(settings_overrides=None):
    app = Flask(__name__)
    load_dotenv()
    configure_settings(app, settings_overrides)
    configure_blueprints(app)
    database.Database.init(app.config.get('MONGO_URI'),app.config.get('DB_NAME'))
    return app


def configure_settings(app, settings_override):
    app.config.from_object(ProdConfig)
    if settings_override:
        app.config.from_object(settings_override)


def configure_blueprints(app):
    app.register_blueprint(api)
    app.register_blueprint(errors)