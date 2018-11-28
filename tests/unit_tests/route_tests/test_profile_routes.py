
from app import app


def test_get_msisdn_status():
    msisdn = '712306172'

    # Act

    result = app.test_client().get(
        '/inservices/api/v1.0/profile/status/<msisdn>', msisdn)

    # Assert
    isinstance(result, dict)


def test_get_msisdn_balance():
    msisdn = '712306172'

    # Act

    result = app.test_client().get(
        '/inservices/api/v1.0/profile/balance/<msisdn>', msisdn)

    # Assert
    isinstance(result, dict)
    