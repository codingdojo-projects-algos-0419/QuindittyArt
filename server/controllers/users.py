from flask import render_template, request, redirect, session, url_for, flash
from sqlalchemy import func
from app import db
from server.models.posts import Post
from server.models.users import User
from server.models.backgrounds import Background
from server.models.comments_table import Comment

def login_and_registration():
    background = Background.query.filter_by(current = 1).first()
    content_background = Post.query.get(2)
    if background and content_background:
        backgrounds = "<style> .wrapper{background-image: url('.."+ url_for('static', filename=background.filename) + "') } .new_account_form{ background-color: " + content_background.text_content + " } .header_right{ background-color: " + content_background.text_content + " }</style>"
        return render_template('Log_and_reg.html', backgrounds=backgrounds)
    return render_template('Log_and_reg.html')

def create():
    errors = User.validate(request.form)
    if errors:
        for error in errors:
            flash(error)
        return redirect(url_for('users:login_and_registration'))
    user_id = User.create(request.form)
    session['user_id'] = user_id
    return redirect(url_for("dashboard"))

def login():
    valid, response = User.login_helper(request.form)
    if not valid:
        flash(response)
        return redirect(url_for("users:login_and_registration"))
    session['user_id'] = response
    return redirect(url_for("dashboard"))

def logout():
    session.clear()
    return redirect(url_for("dashboard"))

def post(post_id):
    user = User.query.get(session['user_id'])
    post = Post.query.filter_by(id=post_id)
    return render_template('post.html', user=user, post=post)

def account_page(user_id):
    current_user = User.query.get(session['user_id'])
    user = User.query.get(user_id)
    comments = Comment.comments_from_user(user_id=user_id)
    background = Background.query.filter_by(current = 1).first()
    content_background = Post.query.get(2)
    backgrounds = "<style> .wrapper{background-image: url('../.."+ url_for('static', filename=background.filename) + "') } .edit_form{ background-color: " + content_background.text_content + " } .gallery{ background-color: " + content_background.text_content + " } .header_right{ background-color: " + content_background.text_content + " }</style>"
    if current_user.id == user.id or current_user.admin_lvl == 2:
        return render_template('account_page.html', current_user=current_user, user=user, comments=comments, backgrounds=backgrounds)
    return redirect(url_for('dashboard'))

def editing(user_id):
    user = User.query.get(user_id)
    errors = User.edit_validate(request.form)
    if errors:
        for error in errors:
                flash(error)
        return redirect(url_for('users:edit'))
    user.username = request.form['username']
    db.session.commit()
    return redirect(url_for('dashboard'))
