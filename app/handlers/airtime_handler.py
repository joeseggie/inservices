# The airtime_handler.py handles the business logic.

from intelecom.intelecom import INConnection


from app import app


from app.handlers.profile_handler import account_info


from app.models.user import User


def msisdnValidity(msisdn: str, current_user: User) -> bool:
    """Checks whether MSISDN account exists in the database.

    Parameters
    ----------
    msisdn : str
        MSISDN number for the account whose validity is being checked.

    current_user : User
        User performing the MSISDN validity query.

    Returns
    -------
    bool
        Returns True if the MSISDN exists and False otherwise.
    """
    account_details = account_info(msisdn, current_user)
    return msisdn == account_details['mobileNumber']


def account_Balance(msisdn: str, current_user: User) ->int:
    """Checks whether MSISDN has balance on the account.

    Parameters
    ----------
    msisdn : str
        MSISDN number for the account whose balance is being required.

    current_user : User
        User performing the account balance status query.

    Returns
    -------
    str
        Returns the balance attached on the MSISDN.
    """
    account_details = account_info(msisdn, current_user)
    msisdn_balance = float(account_details['balance'])
    return msisdn_balance


def account_bal_GTE(msisdn: str, amount: float, current_user: User) -> bool:
    """Checks whether MSISDN account balance is GTE to the supplied Amount.

    Parameters
    ----------
    msisdn : str
        MSISDN number for the account whose balance is matched aganist.
    amount : float
        Money to be credited or debited on a MSISDN account.
    current_user : User
        User performing the balance comparison query.

    Returns
    -------
    bool
        Returns True if the MSISDN account balance is GTE, False otherwise.
    """
    account_details = account_info(msisdn, current_user)
    msisdn_balance = float(account_details['balance'])
    return msisdn_balance >= amount


def account_bal_LTE(msisdn: str, amount: float, current_user: User) -> bool:
    """Checks whether MSISDN account balance is GTE to the supplied Amount.

    Parameters
    ----------
    msisdn : str
        MSISDN number for the account whose balance is matched aganist.
    amount : float
        Money to be credited or debited on a MSISDN account.
    current_user : User
        User performing the balance comparison query.

    Returns
    -------
    bool
        Returns True if the MSISDN account balance is GTE, False otherwise.
    """
    account_details = account_info(msisdn, current_user)
    msisdn_balance = float(account_details['balance'])
    return msisdn_balance <= amount


def debit_account(msisdn: str, amount: float, current_user: User):
    """Debits the MSISDN account with the new amount..

    Parameters
    ----------
    msisdn : str
        MSISDN number for the account whose balance to be debited.
    amount : float
        Money to be debited on a MSISDN account.
    current_user : User
        User performing the deduction amount query.

    Returns
    -------
    bool
        Returns True if the MSISDN account balance is debited, False otherwise.
    """
    with INConnection(
            app.config['IN_SERVER']['HOST'],
            current_user.mml_username,
            current_user.mml_password,
            app.config['IN_SERVER']['PORT'],
            app.config['IN_SERVER']['BUFFER_SIZE']) as in_connection:

        return in_connection.debit_account(
            msisdn,
            amount,
            current_user.mml_username
        )


def credit_account(msisdn: str, amount: float, current_user: User):
    """Credits the MSISDN account with a new amount.

    Parameters
    ----------
    msisdn : str
        MSISDN number for the account whose balance is to be credited.
    amount : float
        Money to be credited on a MSISDN account.
    current_user : User
        User performing the crediting account query.

    Returns
    -------
    bool
        Returns True if the MSISDN account balance is credited False otherwise.
    """
    with INConnection(
            app.config['IN_SERVER']['HOST'],
            current_user.mml_username,
            current_user.mml_password,
            app.config['IN_SERVER']['PORT'],
            app.config['IN_SERVER']['BUFFER_SIZE']) as in_connection:

        return in_connection.credit_account(
            msisdn,
            amount,
            current_user.mml_username
        )
