from flask import Blueprint, jsonify, request

from app.handlers.airtime_handler import credit_account, debit_account
from app.models.user import User


blueprint_api_airtime = Blueprint('blueprint_api_airtime', __name__)


@blueprint_api_airtime.route('/')
def index():
    return 'Hello World'


@blueprint_api_airtime.route('/debit', method=['POST'])
def debit_msisdn_account():
    """
    Debits the MSISDN account
    Returns
    -------
    json
        Transaction details and the amount deducted.
    """
    current_user = User(mml_username='pkgmml', mml_password='pkgmml99')
    data = request.get_json()
    results = debit_account(data['msisdn'], data['amount'], current_user)
    if results:
        operationResult = 'Ok'
    else:
        operationResult = 'Failed'
    debit_response = {
        'transactionId': results['transactionId'],
        'transactionDateTime': results['transactionDateTime'],
        'operationResult': operationResult,
        'msisdn': results['msisdn'],
        'amount': results['amount']
    }
    return jsonify(debit_response), 200


@blueprint_api_airtime.route('/credit', method=['POST'])
def credit_msisdn_account():
    """
    Credits the MSISDN account
    Returns
    -------
    json
        Transaction details and the amount credited.
    """
    current_user = User(mml_username='pkgmml', mml_password='pkgmml99')
    data = request.get_json()
    results = credit_account(data['msisdn'], data['amount'], current_user)
    if results:
        operationResult = 'Ok'
    else:
        operationResult = 'Failed'
    credit_response = {
        'transactionId': results['transactionId'],
        'transactionDateTime': results['transactionDateTime'],
        'operationResult': operationResult,
        'msisdn': results['msisdn'],
        'amount': results['amount']
    }
    return jsonify(credit_response), 200
