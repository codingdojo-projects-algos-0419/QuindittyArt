from flask import render_template, request, redirect, session, url_for, flash
from sqlalchemy import desc
from config import db
from server.models.users import User
from server.models.posts import Post
from server.models.backgrounds import Background

def dashboard():
    posts = Post.realposts()
    background = Background.query.filter_by(current = 1).first()
    content_background = Post.query.get(2)
    if background and content_background:
        backgrounds = "<style> .wrapper{background-image: url('.."+ url_for('static', filename=background.filename) + "') } .gallery{ background-color: " + content_background.text_content + " } .header_right{ background-color: " + content_background.text_content + " }</style>"
        if 'user_id' in session:
            user = User.query.get(session['user_id'])
            return render_template('dashboard.html', user=user, posts=posts, backgrounds=backgrounds)
        return render_template('dashboard.html', posts=posts, backgrounds=backgrounds)
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        return render_template('dashboard.html', user=user, posts=posts)
    return render_template('dashboard.html')

def about_me():
    about_me = Post.query.get(1)
    admin = False
    background = Background.query.filter_by(current = 1).first()
    content_background = Post.query.get(2)
    backgrounds = "<style> .wrapper{background-image: url('.."+ url_for('static', filename=background.filename) + "') } .about_me{ background-color: " + content_background.text_content + " } </style>"
    if 'user_id' in session:
        user = User.query.get(session['user_id'])
        if user.admin_lvl == 2:
            admin = True
        return render_template('about_me.html', user=user, about_me=about_me, backgrounds=backgrounds, admin=admin)
    return render_template('about_me.html', about_me=about_me, backgrounds=backgrounds, admin=admin)

