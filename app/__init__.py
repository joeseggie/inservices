from app.inservices import app, db, login, logger

from app.routes.accounts import blueprint_api_accounts
from app.routes.airtime import blueprint_api_airtime
from app.routes.profile import blueprint_api_profile
from app.routes.services import blueprint_api_services


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
