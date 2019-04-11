from flask import render_template, request, redirect, session, url_for, flash
from werkzeug.utils import secure_filename
from config import db, app
from server.models.posts import Post
from server.models.users import User


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def new_post():
    user = User.query.get(session['user_id'])
    return render_template('posts_new.html', user=user)

def create():
        if 'file' not in request.files:
                flash('No file part')
                return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
                flash('No selected file')
                return redirect(request.url)
        if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
                errors = Post.validate(request.form)
                if errors:
                        for error in errors:
                                flash(error)
                        return redirect(url_for('posts:create'))
                Post.create(request.form, session['user_id'])
                return redirect(url_for('dashboard'))
        return redirect(url_for('posts:create'))

def view_post(post_id):
        post = Post.query.get(post_id)
        return render_template('post.html', post=post)



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
