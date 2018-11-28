"""Handler that caters for the cross functionality features.
"""
from datetime import datetime
import logging
from random import randint
import re

from app import logger


def msisdn_is_valid(msisdn: str) -> bool:
    """Checks if mobile number is valid.

    Parameters
    ----------
    msisdn : str
        Mobile number that is being validated.

    Returns
    -------
    bool
        True, if mobile number is valid. Otherwise, False.
    """
    valid_msisdn = False
    valid_msisdn_pattern = r'\b(71)\d{7}|(4)\d{8}\b'
    if re.match(valid_msisdn_pattern, msisdn):
        valid_msisdn = True

    return valid_msisdn


def write_log(log_level: int, platform: str, category: str, message: str, user: str):
    """Write custom log.

    Parameters
    ----------
    platform : str
        Platform runnning the service or application.
    category : str
        Log category.
    message : str
        Log message.
    user : str
        User performing the action.
    """
    if log_level == logging.INFO:
        logger.info('%s - %s - %s - %s', platform, category, message, user)
    elif log_level == logging.WARNING:
        logger.warning('%s - %s - %s - %s', platform, category, message, user)
    elif log_level == logging.ERROR:
        logger.error('%s - %s - %s - %s', platform, category, message, user)
    elif log_level == logging.CRITICAL:
        logger.critical('%s - %s - %s - %s', platform, category, message, user)
    else:
        logger.info('%s - %s - %s - %s', platform, category, message, user)


def transactionid_generator():
    """Generates the transaction Id.
    """
    now = datetime.today()
    date_part = now.strftime('%Y%m%d%H%M%S')
    random_part = randint(1000, 9999)
    return f'{date_part}{random_part}'


class InvalidMsisdnError(ValueError):
    """Error raised when MSISDN is invalid"""
    pass
