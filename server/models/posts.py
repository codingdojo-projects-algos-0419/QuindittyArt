from sqlalchemy.sql import func
from config import db
from server.models.likes_table import likes_table
from server.models.comments_table import Comment

class Post(db.Model):
    __tablename__ = 'posts'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(
        db.Integer, db.ForeignKey("users.id"), nullable=False
    )
    title = db.Column(db.String(255), nullable=False)
    filename = db.Column(db.Text, nullable=False)
    text_content = db.Column(db.Text, nullable=False)
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
    post_comments = db.relationship('Comment', back_populates='post')
    users_who_like_this_post = db.relationship('User', secondary=likes_table, cascade='all')

    def not_liked(self):
        user = User.query.get(session['user_id'])
        if user in self.user_who_like_this_post:
            return False
        else:
            return True

    def likes(self):
        likes = 0 
        likes_users = self.users_who_like_this_post
        for user in likes_users:
            likes += 1
        return likes

    @classmethod
    def validate(cls, form, filename):
        errors = []
        if len(form['title']) > 255:
            errors.append("Title cannot exceed 255 characters in length.")
        if len(form['title']) <= 2:
            errors.append("Title mush consist of at least 2 characters.")
        if len(filename) > 400:
            errors.append("filename cannot exceed 400 characters in length.")
        if len(form['text_content']) > 500:
            errors.append("Post cannot exceed 500 characters in length.")
        if len(form['text_content']) < 3:
            errors.append("Post mush consist of at least 3 characters.")
        return errors

    @classmethod
    def create(cls, form, filename, user_id):
        post = cls(title=form['title'], text_content=form['text_content'], filename=filename,  user_id=user_id)
        db.session.add(post)
        db.session.commit()


    @classmethod
    def realposts(cls):
        return cls.query.filter(cls.id !=1, cls.id !=2).order_by(cls.created_at.desc()).all()
