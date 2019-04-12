import os
from flask import render_template, request, redirect, session, url_for, flash
from werkzeug.utils import secure_filename
from config import db, app
from server.models.posts import Post
from server.models.users import User
from server.models.backgrounds import Background
from server.models.comments_table import Comment


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def new_post():
        user = User.query.get(session['user_id'])
        background = Background.query.filter_by(current = 1).first()
        if user.admin_lvl == 2:
                return render_template('new_post.html', user=user, background=background)
        return redirect(url_for('dashboard'))

def create():
        if 'content' not in request.files:
                flash('No file part')
                return redirect(url_for('posts:new_post'))
        file = request.files['content']
        if file.filename == '':
                flash('No selected file')
                return redirect(url_for('posts:new_post'))
        if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                filename = "images/" + secure_filename(file.filename)
                errors = Post.validate(request.form, filename=filename)
                if errors:
                        for error in errors:
                                flash(error)
                        return redirect(url_for('posts:new_post'))
                Post.create(request.form, user_id=session['user_id'], filename=filename)
                return redirect(url_for('dashboard'))
        return redirect(url_for('posts:new_post'))

def view_post(post_id):
        user = User.query.get(session['user_id'])
        post = Post.query.get(post_id)
        background = Background.query.filter_by(current = 1).first()
        comments = Comment.query.filter_by(post_id=post_id)
        return render_template('post.html', user=user, post=post, background=background, comments=comments)



def like(post_id):
        user = User.query.get(session['user_id'])
        post = Post.query.get(post_id)
        post.users_who_like_this_post.append(user)
        db.session.commit()
        return redirect(url_for('dashboard'))


def delete(post_id):
        post = Post.query.get(post_id)
        admin = User.query.get(session['user_id'])
        if admin.admin_lvl == 2:
                db.session.delete(post)
                db.session.commit()
        return redirect(url_for('dashboard'))

def comment(post_id):
        Comment.create(post_id=post_id, content=request.form['content'])
        return redirect(url_for('posts:view_post', post_id=post_id))

def delete_comment(comment_id, post_id):
        comment = Comment.query.filter_by(id=comment_id).first()
        db.session.delete(comment)
        db.session.commit()
        return redirect(url_for('posts:view_post', post_id=post_id))
