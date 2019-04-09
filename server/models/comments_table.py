from sqlalchemy.sql import func
from config import db

comments_table=db.Table('likes',
    db.Column(
        'post_id',
        db.Integer,db.ForeignKey(
            'posts.id', ondelete="cascade"
        ),
        primary_key=True
    ),
    db.Column(
        'user_id', db.Integer, db.ForeignKey('users.id'), 
        primary_key=True
    ),
    db.Column(
      'content', db.Text, nullable=False
    ),
    db.Column(
        'created_at', db.DateTime,
        server_default=func.now()
    ),
)

