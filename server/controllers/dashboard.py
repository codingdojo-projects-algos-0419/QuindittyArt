from flask import render_template, request, redirect, session, url_for, flash
from config import db
from server.models.users import User
from server.models.posts import Post

def root():
    posts = Post.query.all()
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        
        return redirect(url_for('dashboard'), user=user, posts=posts)
    return redirect(url_for('dashboard'), posts=posts)
