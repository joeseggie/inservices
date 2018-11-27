from flask import Blueprint


import json


from intelecom.intelecom import INConnection


from flask import Blueprint, request, jsonify, session, make_response


from app import app


from app.handlers.airtime_handler import debit_account, credit_account


from app.models.user import User


blueprint_api_airtime = Blueprint('blueprint_api_airtime', __name__)


@blueprint_api_airtime.route('/')
def index():
    return 'Hello World'


@blueprint_api_airtime.route('/debit/debit_account', method=['POST'])
def debit_msisdn_account():
    # TODO implement the URl link
    debit_details = request.get_json()
    if debit_details.status_code == debit_details.codes.ok:
        operationResult = 'Ok'
    else:
        operationResult = 'Failed'
    debit_response = {
        'transactionId': debit_details['current_user'],
        'transactionDateTime': 'transactionDateTime',
        'operationResult': operationResult,
        'msisdn': debit_details['msisdn'],
        'amount': debit_details['amount']
    }
    return jsonify(debit_response), 200


@blueprint_api_airtime.route('/credit/credit_account', method=['POST'])
def credit_msisdn_account():
    # TODO implement the URl link
    credit_details = request.get_json()
    credit_account(credit_details['msisdn'], credit_details['amount'], credit_details['current_user'])
    if credit_details.status_code == credit_details.codes.ok:
        operationResult = 'Ok'
    else:
        operationResult = 'Failed'
    credit_response = {
        'transactionId': credit_details['current_user'],
        'transactionDateTime': 'transactionDateTime',
        'operationResult': operationResult,
        'msisdn': credit_details['msisdn'],
        'amount': credit_details['amount']
    }
    return jsonify(credit_response), 200


