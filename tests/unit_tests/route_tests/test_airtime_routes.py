import json

from app import app


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
