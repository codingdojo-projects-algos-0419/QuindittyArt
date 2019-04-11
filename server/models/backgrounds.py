from sqlalchemy.sql import func
from config import db

class Background(db.Model):
  __tablename__ = 'backgrounds'
  id = db.Column(db.Integer, primary_key=True)
  filename = db.Column(db.Text, nullable=False)
  current = db.Column(db.Integer, nullable=False, default=0)
  created_at = db.Column(
    db.DateTime, server_default=func.now()
  )
  updated_at = db.Column(
    db.DateTime, server_default=func.now(), onupdate=func.now()
  )

  @classmethod
  def validate(cls, form):
    errors = []
    if len(form['filename']) > 50:
      errors.append("filename cannot exceed 400 characters in length.")
    return errors


  @classmethod
  def create(cls, form, filename):
    post = cls(content=form['title'], text_content=form['text_content'], filename=filename)
    db.session.add(post)
    db.session.commit()