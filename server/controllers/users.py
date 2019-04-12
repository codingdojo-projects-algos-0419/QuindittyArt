from flask import render_template, request, redirect, session, url_for, flash
from sqlalchemy import func
from server.models.posts import Post
from server.models.users import User
from server.models.backgrounds import Background

def login_and_registration():
    background = Background.query.filter_by(current = 1).first()
    return render_template('Log_and_reg.html', background=background)

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
        return redirect(url_for("users:new"))
    session['user_id'] = response
    return redirect(url_for("dashboard"))

def logout():
    session.clear()
    return redirect(url_for("dashboard"))

def post(post_id):
    user = User.query.get(session['user_id'])
    post = Post.query.filter_by(id=post_id)
    return render_template('post.html', user=user, post=post)

def edit(user_id):
    user = User.query.get(user_id)
    return render_template('user_edit.html', user=user)

def editing(user_id):
    user = User.query.get(user_id)
    errors = User.validate(request.form)
    if errors:
        for error in errors:
                flash(error)
        return redirect(url_for('users:edit'))
    user.username = request.form['username']
    db.session.commit()
    return redirect(url_for('dashboard'))
