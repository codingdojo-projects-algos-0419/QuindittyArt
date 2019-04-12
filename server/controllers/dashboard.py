from flask import render_template, request, redirect, session, url_for, flash
from config import db
from server.models.users import User
from server.models.posts import Post
from server.models.backgrounds import Background

def dashboard():
    posts = Post.query.all()
    background = Background.query.filter_by(current = 1).first()
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        return render_template('dashboard.html', user=user, posts=posts, background=background)
    return render_template('dashboard.html', posts=posts, background=background)
