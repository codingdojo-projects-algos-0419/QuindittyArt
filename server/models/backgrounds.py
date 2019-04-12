from sqlalchemy.sql import func
from config import db

class Background(db.Model):
  __tablename__ = 'backgrounds'
  id = db.Column(db.Integer, primary_key=True)
  title = db.Column(db.Text, nullable=False)
  filename = db.Column(db.Text, nullable=False)
  current = db.Column(db.Integer, nullable=False, default=0)
  created_at = db.Column(
    db.DateTime, server_default=func.now()
  )
  updated_at = db.Column(
    db.DateTime, server_default=func.now(), onupdate=func.now()
  )

  @classmethod
  def create(cls, title, filename):
    background = cls(title=title, filename=filename)
    db.session.add(background)
    db.session.commit()