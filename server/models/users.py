from sqlalchemy.sql import func
from config import db, bcrypt
from server.models.likes_table import likes_table
from server.models.comments_table import Comment
from server.models.posts import Post


class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255), nullable=False)
    pw_hash = db.Column(db.String(255), nullable=False)
    admin_lvl = db.Column(db.Integer, nullable=False, default=1)
    created_at = db.Column(
        db.DateTime, server_default=func.now()
    )
    updated_at = db.Column(
        db.DateTime, server_default=func.now(), onupdate=func.now()
    )
    users_comments = db.relationship('Comment', back_populates='user', cascade='all')
    posts_this_user_likes = db.relationship('Post', secondary=likes_table, cascade='all')


    def __repr__(self):
        return "<User: %s>" % self.username

    def __str__(self):
        return "<User: %s>" % self.username

    @classmethod
    def validate(cls, form):
        errors = []
        existing_username = cls.query.filter_by(username=form['username']).first()
        if existing_username:
            errors.append("Username already in use.")
        if len(form['username']) < 2:
            errors.append("Username must be at least 2 characters long.")
        if len(form['username']) < 2:
            errors.append("Username must be at least 2 characters long.")
        if len(form['password']) < 8:
            errors.append("Password must be at least 8 characters long.")
        
        if form['password'] != form['confirm']:
            errors.append('Passwords must match')

        return errors

    @classmethod
    def edit_validate(cls, form):
        errors = []
        existing_username = cls.query.filter_by(username=form['username']).first()
        if existing_username:
            errors.append("Username already in use.")
        if len(form['username']) < 2:
            errors.append("Username must be at least 2 characters long.")
        if len(form['username']) < 2:
            errors.append("Username must be at least 2 characters long.")
        return errors

    @classmethod
    def create(cls, form):
        pw_hash = bcrypt.generate_password_hash(form['password'])
        user = cls(
            username=form['username'],
            pw_hash=pw_hash,
        )
        db.session.add(user)
        db.session.commit()
        return user.id
    
    @classmethod
    def login_helper(cls, form):
        user = cls.query.filter_by(username=form['username']).first()
        if user:
            if bcrypt.check_password_hash(user.pw_hash, form['password']):
                return (True, user.id)
        return (False, "Username or password incorrect.")

    def admin_lvl_increase(self):
        self.admin_lvl = 2
        db.session.commit()

    def admin_lvl_decrease(self):
        self.admin_lvl = 1
        db.session.commit()
