from flask import render_template, request, redirect, session, url_for, flash
from config import db
from server.models.users import User
from server.models.posts import Post
from server.models.backgrounds import Background

def dashboard():
    posts = Post.query.filter(id!=1).all()
    background = Background.query.filter_by(current = 1).first()
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        return render_template('dashboard.html', user=user, posts=posts, background=background)
    return render_template('dashboard.html', posts=posts, background=background)

def about_me():
    user = User.query.get(session['user_id'])
    about_me = Post.query.get(1)
    background = Background.query.filter_by(current=1).first()
    return render_template('about_me.html', user=user, about_me=about_me, background=background)

