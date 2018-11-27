# Testing the credit/Debit airtime handler.
from unittest.mock import Mock, patch

from intelecom.intelecom import INConnection


from app.models.user import User


from app.handlers.airtime_handler import (
    msisdnValidity,
    account_Balance,
    account_bal_GTE,
    account_bal_LTE,
    debit_account,
    credit_account
)


def test_isvalid_msid():
    msisdn = '712306172'
    current_user = User(mml_username='pkgmml', mml_password='pkgmml99')
    # Act
    result = msisdnValidity(msisdn, current_user)

    # Assert
    assert isinstance(result, bool)


def test_balance_status():
    msisdn = '712306172'
    current_user = User(mml_username='pkgmml', mml_password='pkgmml99')

    # Act
    result = account_Balance(msisdn, current_user)

    # Assert
    assert isinstance(result, float)


def test_check_account_bal_GTE():
    msisdn = '712306172'
    amount = 2000.0
    current_user = User(mml_username='pkgmml', mml_password='pkgmml99')

    # Act
    result = account_bal_GTE(msisdn, amount, current_user)

    # Assert
    assert isinstance(result, bool)


def test_check_account_bal_LTE():
    msisdn = '712306172'
    amount = 2000.0
    current_user = User(mml_username='pkgmml', mml_password='pkgmml99')
    # Act
    result = account_bal_LTE(msisdn, amount, current_user)

    # Assert
    assert isinstance(result, bool)


@patch.object(INConnection, 'logout')
@patch.object(INConnection, 'login')
@patch.object(INConnection, 'debit_account')
def test_debit_msisdn_account(mock_debit_amount, mock_login, mock_logout):
    mock_debit_amount.return_value = True
    msisdn = '712306172'
    amount = 100.0
    mock_current_user = Mock()

    # Act
    result = debit_account(msisdn, amount, mock_current_user)

    # Assert
    assert isinstance(result, bool)


@patch.object(INConnection, 'logout')
@patch.object(INConnection, 'login')
@patch.object(INConnection, 'credit_account')
def test_credit_msisdn_account(mock_credit_amount, mock_login, mock_logout):
    mock_credit_amount.return_value = True
    mock_current_user = Mock()
    msisdn = '712306172'
    amount = 100.0
    # Act
    result = credit_account(msisdn, amount, mock_current_user)

    # Assert
    assert isinstance(result, bool)
