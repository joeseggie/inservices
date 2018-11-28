import json

from app import app

from app.routes import airtime
from unittest.mock import patch


@patch.object(airtime, 'debit_msisdn_account')
def test_debit_account_post():
    sampleData = {
        'msisdn': '712306172',
        'amount': 1000.0
    }

    # Act

    result = app.test_client().post(
        '/inservices/api/v1.0/airtime/debit',
        data=json.dumps(sampleData),
        content_type='application/json',)

    # Assert
    isinstance(result, dict)


@patch.object(airtime, 'credit_msisdn_account')
def test_credit_account_post():
    sampleData = {
        'msisdn': '712306172',
        'amount': 1000.0
    }

    # Act

    result = app.test_client().post(
        '/inservices/api/v1.0/airtime/credit',
        data=json.dumps(sampleData),
        content_type='application/json',)

    # Assert
    isinstance(result, dict)
