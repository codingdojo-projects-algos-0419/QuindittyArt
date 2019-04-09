from sqlalchemy.sql import func
from config import db
from server.models.likes_table import likes_table

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id"), nullable=False
    )
    author = db.Column(db.String(255), nullable=False)
    text_content = db.Column(db.Text, nullable=False)
    picture_content = db.Column(db.)
    created_at = db.Column(
        db.DateTime, server_default=func.now()
    )
    updated_at = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now()
    )
    user=db.relationship(
        'User', foreign_keys=[user_id], backref=db.backref(
            "posts", cascade="all, delete-orphan"
            )
    )
    users_who_like_this_post = db.relationship('User', secondary=likes_table, cascade='all')

    def likes(self):
        likes = 0 
        likes_users = self.users_who_like_this_post
        for user in likes_users:
            likes += 1
        return likes

    @classmethod
    def validate(cls, form):
        errors = []
        if len(form['content']) > 400:
            errors.append("Post cannot exceed 400 characters in length.")
        if len(form['content']) < 10:
            errors.append("Post mush consist of at least 10 characters.")
        return errors

    @classmethod
    def create(cls, form, user_id):
        post = cls(author=form['author'], content=form['content'],  user_id=user_id)
        db.session.add(post)
        db.session.commit()


    @classmethod
    def get_posts_from_users(cls, user_ids=None):
        if not user_ids:
            return cls.query.order_by(cls.created_at.desc()).all()
        return cls.query.filter(cls.user_id.in_(user_ids)).order_by(cls.created_at.desc()).all()
