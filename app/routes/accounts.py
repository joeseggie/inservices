from flask import Blueprint


blueprint_api_accounts = Blueprint('blueprint_api_accounts', __name__)


@blueprint_api_accounts.route('/')
def index():
    return 'Hello World'
