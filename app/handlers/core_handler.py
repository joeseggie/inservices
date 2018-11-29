"""Handler that caters for the cross functionality features.
"""
from datetime import datetime
from random import randint
import re


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


def transactionid_generator():
    """Generates the transaction Id.
    """
    now = datetime.today()
    date_part = now.strftime('%Y%m%d%H%M%S')
    random_part = randint(1000, 9999)
    return (f'{date_part}{random_part}', now.strftime('%Y-%m-%d %H:%M:%S'))
