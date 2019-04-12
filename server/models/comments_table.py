from sqlalchemy.sql import func
from flask import session
from config import db

class Comment(db.Model):
  __tablename__ = 'comments'
  id = db.Column(db.Integer, primary_key=True)
  post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), nullable=False)
  user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
  content = db.Column(db.Text, nullable=False)
  created_at = db.Column(
    db.DateTime, server_default=func.now()
  )
  updated_at = db.Column(
    db.DateTime, server_default=func.now(), onupdate=func.now()
  )
  user = db.relationship('User', back_populates='users_comments')
  post = db.relationship('Post', back_populates='post_comments')

  @classmethod
  def create(cls, content, post_id):
    comment = cls(user_id=session['user_id'], post_id=post_id, content=content)
    db.session.add(comment)
    db.session.commit()