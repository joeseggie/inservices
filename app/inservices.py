import logging
from logging.handlers import TimedRotatingFileHandler
import os

from flask import Flask
from flask_login import LoginManager
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

from app.routes.accounts import blueprint_api_accounts
from app.routes.airtime import blueprint_api_airtime
from app.routes.profile import blueprint_api_profile
from app.routes.services import blueprint_api_services


app = Flask(__name__, instance_relative_config=True)

CONFIG_ENV = {
    'default': 'config.default.Config',
    'development': 'config.development.DevelopmentConfig',
    'production': 'config.production.ProductionConfig',
    'testing': 'config.testing.TestingConfig'
}


def setup_logging():
    """Setup module logging
    """
    log_date_format = '%Y-%m-%d %H:%M:%S'
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt=log_date_format)

    rotating_handler = TimedRotatingFileHandler(
        filename='../logs/inservices.log',
        encoding='utf-8',
        when='midnight',
        utc=True
    )
    rotating_handler.setFormatter(formatter)

    app_logger = logging.getLogger(__name__)
    app_logger.setLevel(logging.INFO)

    app_logger.addHandler(rotating_handler)

    return app_logger


def config_app(application):
    """Application configuration function.

    Parameters
    ----------
    application: Flask
        Flask application to configure.
    """
    config_name = os.getenv('FLASK_ENV', 'default')
    application.config.from_pyfile('config.py')
    application.config.from_object(CONFIG_ENV[config_name])


app = Flask(__name__, instance_relative_config=True)
config_app(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login = LoginManager(app)
logger = setup_logging()

# api blueprints
app.register_blueprint(
    blueprint_api_accounts,
    url_prefix='/inservices/api/v1.0/accounts'
)
app.register_blueprint(
    blueprint_api_airtime,
    url_prefix='/inservices/api/v1.0/airtime'
)
app.register_blueprint(
    blueprint_api_profile,
    url_prefix='/inservices/api/v1.0/profile'
)
app.register_blueprint(
    blueprint_api_services,
    url_prefix='/inservices/api/v1.0/services'
)
