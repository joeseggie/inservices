
import uuid

from flask import jsonify, make_response, request
from intelecom.intelecom import (
    INLoginError,
    INLogoutError,
    INQueryError,
    MsisdnMatchError
)
import jwt

from app.decorators import token_required
from app import app, logger
from app.models.user import User
from app.models.usertoken import UserToken
from app.routes import blueprint_api_profile
from app.handlers.profile_handler import INRequestHandler


@blueprint_api_profile.route('/balance/<msisdn>')
@token_required
def balance(current_user: User, transaction_id: str, msisdn: str):
    """Get MSISDN balance
    """
    try:
        request_manager = INRequestHandler(
            host=app.config['IN_SERVER']['HOST'],
            port=app.config['IN_SERVER']['PORT'],
            buffer_size=app.config['IN_SERVER']['BUFFER_SIZE']
        )

        logger.info(
            'API - SYSTEM - %s - BALANCE query for %s  - %s',
            transaction_id,
            msisdn,
            current_user.username
        )

        account_info = request_manager.account_info(msisdn, current_user)
        account_balance = {
            'transactionId': transaction_id,
            'mobileNumber': account_info['mobileNumber'],
            'balance': account_info['balance'],
        }

        return jsonify(account_balance), 200

    except INLoginError as login_error:
        logger.error(
            'API - SYSTEM - %s - %s',
            transaction_id,
            login_error.msg
        )
    except INLogoutError as logout_error:
        logger.error(
            'API - SYSTEM - %s - %s',
            transaction_id,
            logout_error.msg
        )
    except MsisdnMatchError as invalid_msisdn_error:
        logger.error(
            'API - SYSTEM - %s - %s',
            transaction_id,
            invalid_msisdn_error.msg
        )
    except INQueryError as in_query_error:
        logger.error(
            'API - SYSTEM - %s - %s',
            transaction_id,
            in_query_error.msg
        )


@blueprint_api_profile.route('/<msisdn>')
@token_required
def info(current_user: User, transaction_id: str, msisdn: str):
    """Get MSISDN account profile.
    """
    try:
        request_manager = INRequestHandler(
            host=app.config['IN_SERVER']['HOST'],
            port=app.config['IN_SERVER']['PORT'],
            buffer_size=app.config['IN_SERVER']['BUFFER_SIZE']
        )

        logger.info(
            'API - SYSTEM - %s - PROFILE query for %s  - %s',
            transaction_id,
            msisdn,
            current_user.username
        )

        account_info = request_manager.account_info(msisdn, current_user)
        account_info['transactionId'] = transaction_id

        return jsonify(account_info), 200

    except INLoginError as login_error:
        logger.error(
            'API - SYSTEM - %s - %s',
            transaction_id,
            login_error.msg
        )
    except INLogoutError as logout_error:
        logger.error(
            'API - SYSTEM - %s - %s',
            transaction_id,
            logout_error.msg
        )
    except MsisdnMatchError as invalid_msisdn_error:
        logger.error(
            'API - SYSTEM - %s - %s',
            transaction_id,
            invalid_msisdn_error.msg
        )
    except INQueryError as in_query_error:
        logger.error(
            'API - SYSTEM - %s - %s',
            transaction_id,
            in_query_error.msg
        )
