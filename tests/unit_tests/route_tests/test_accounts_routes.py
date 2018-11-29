from base64 import b64encode
import pdb
from unittest.mock import Mock, patch

from app import app

import pytest


def test_login_forbidden_no_authorization():
    """Test unauthorized request is forbidden.
    """
    with app.test_client() as app_test:
        response = app_test.get('/inservices/api/v1.0/accounts/login')
        assert response.status_code == 403


def test_login_authorized():
    """Test authorized request returns success HTTP status code.
    """
    with app.test_client() as app_test:
        encoded_credentials = b64encode(b"vasuser:1iyDjV")
        auth = encoded_credentials.decode('utf-8')
        response = app_test.get(
            '/inservices/api/v1.0/accounts/login',
            headers={
                "Authorization": f"Basic { auth }"})
        assert response.status_code == 200


@pytest.mark.skip(reason='Not properly setup')
def test_create_account(mock_is_valid, mock_set_password):
    """Test authorized request returns success HTTP status code.
    """
    mock_is_valid.return_value = True
    mock_set_password.return_value = 'mock_password'
    account_creator = {
        'username': 'mock_user',
        'is_admin': True,
        'is_active': True,
        'can_debit': True,
        'can_credit': True,
        'mml_username': 'mml',
        'mml_password': 'mml_pass',
        'user_type': 'ADMIN'
    }
    with app.test_client() as app_test:
        response = app_test.post(
            '/inservices/api/v1.0/accounts/create',
            data=account_creator,
            content_type='application/json'
        )
        pdb.set_trace()
        assert response.status_code == 200
