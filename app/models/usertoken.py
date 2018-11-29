"""usertoken module.
"""
from datetime import datetime

from app.inservices import db


class UserToken(db.Model):
    """User tokens table"""
    __tablename__ = 'api_user_token'

    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(256))
    created = db.Column(db.DateTime, default=datetime.utcnow)
    user_public_id = db.Column(db.String(50))
