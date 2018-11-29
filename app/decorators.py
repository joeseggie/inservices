"""Custom decorators module.
"""
from functools import wraps
import jwt

from flask import request, jsonify

from app.handlers.core_handler import transactionid_generator
from app.inservices import app
from app.models.user import User


def token_required(func):
    """Decorator for all routes that require a token.

    Parameters
    ----------
    func : function
        Function to be decorated.
    """
    @wraps(func)
    def decorated(*args, **kwargs):
        token = None
        transaction_id, transaction_datetime = transactionid_generator()

        if 'x-access-token' in request.headers:
            token = request.headers['x-access-token']
        if not token:
            return jsonify({
                'transactionId': transaction_id,
                'operationResult': 'TOKEN IS MISSING',
                'transactionDateTime': transaction_datetime
            }), 403

        try:
            data = jwt.decode(token, app.config['SECRET_KEY'])
            current_user = User.query.filter_by(
                public_id=data['public_id']
                ).first()
        except:
            return jsonify({
                'transactionId': transaction_id,
                'operationResult': 'INVALID TOKEN',
                'transactionDateTime': transaction_datetime
            }), 403

        return func(
            current_user,
            transaction_id,
            transaction_datetime,
            *args,
            **kwargs)

    return decorated
