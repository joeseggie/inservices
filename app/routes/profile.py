from flask import Blueprint, request, jsonify


from app.handlers.profile_handler import profile_status, account_balance

from app.models.user import User

blueprint_api_profile = Blueprint('blueprint_api_profile', __name__)


@blueprint_api_profile.route('/')
def index():
    return 'Hello World'


@blueprint_api_profile.route('/balance/<msisdn>', method=['GET'])
def get_msisdn_balance():
    """
    Gets the currrent status of the MSISDN account
    Parameters
    ----------
    msisdn : str
        MSISDN number for the account whose balance is being required.
    Returns
    -------
    json
        Transaction details and the balance of the account.
    """
    current_user = User(mml_username='pkgmml', mml_password='pkgmml99')
    data = request.get_data()
    results = profile_status(data['msisdn'], current_user)
    status_response = {
        'transactionId': results['transactionId'],
        'transactionDateTime': results['transactionDateTime'],
        'msisdn': results['msisdn'],
        'status': results['status']
    }

    return jsonify(status_response), 200


@blueprint_api_profile.route('/status/<msisdn>', method=['GET'])
def get_msisdn_status():
    """
    Gets the currrent status of the MSISDN account
    Parameters
    ----------
    msisdn : str
        MSISDN number for the account whose status is being required.
    Returns
    -------
    json
        Transaction details and the status of the account.
    """
    current_user = User(mml_username='pkgmml', mml_password='pkgmml99')
    data = request.get_data()
    results = account_balance(data['msisdn'], current_user)
    balance_response = {
        'transactionId': results['transactionId'],
        'transactionDateTime': results['transactionDateTime'],
        'msisdn': results['msisdn'],
        'balance': results['balance']
    }
    return jsonify(balance_response), 200
