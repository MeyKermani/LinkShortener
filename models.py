from datetime import datetime
from app import db


class ShortUrls(db.Model):
    """ A Class which represents the database structure for ShortURLs Table """
    id = db.Column(db.Integer, primary_key=True)
    original_url = db.Column(db.String(500), nullable=False)
    short_id = db.Column(db.String(20), nullable=False, unique=True)
    created_at = db.Column(db.DateTime(), default=datetime.now(), nullable=False)
