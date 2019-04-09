from sqlalchemy.sql import func
from config import db

class Background(db.Model):
    __tablename__ = 'backgrounds'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    picture = db.Column(db.BigInteger, nullable=False)
    created_at = db.Column(
        db.DateTime, server_default=func.now()
    )
    updated_at = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now()
    )
