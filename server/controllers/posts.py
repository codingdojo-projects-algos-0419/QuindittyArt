from flask import render_template, request, redirect, session, url_for, flash
from config import db
from server.models.posts import Post
from server.models.users import User


def new_post():
    user = User.query.get(session['user_id'])
    return render_template('posts_new.html', user=user)


def create():
    errors = Post.validate(request.form)
    if errors:
        for error in errors:
                flash(error)
        return redirect(url_for('dashboard'))
    post.create(request.form, session['user_id'])
    return redirect(url_for("post_list"))


def like(post_id):
    user = User.query.get(session['user_id'])
    post = Post.query.get(post_id)
    post.users_who_like_this_post.append(user)
    db.session.commit()
    return redirect(url_for('post_list'))


def delete(post_id):
    post = Post.query.get(post_id)
    if post.user_id == session['user_id']:
        db.session.delete(post)
        db.session.commit()
    return redirect(url_for('post_list'))
