import os
from flask import render_template, request, redirect, session, url_for, flash
from werkzeug.utils import secure_filename
from config import db, app
from server.models.posts import Post
from server.models.users import User
from server.models.backgrounds import Background


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif'])


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def admin_page():
  user = User.query.get(session['user_id'])
  available_backgrounds = Background.query.filter_by(current = 0).all()
  background = Background.query.filter_by(current = 1).first()
  content_background = Post.query.get(2)
  if user.admin_lvl == 2:
    user_list = User.query.all()
    if available_backgrounds:
      if background and content_background:
        backgrounds = "<style> .wrapper{background-image: url('.."+ url_for('static', filename=background.filename) + "') } .user_list{ background-color: " + content_background.text_content + " } .background_selection{ background-color: " + content_background.text_content + " } .header_right{ background-color: " + content_background.text_content + " }</style>"
        return render_template('admin_page.html', user=user, user_list=user_list, available_backgrounds=available_backgrounds, backgrounds=backgrounds)
      return render_template('admin_page.html', user=user, user_list=user_list, available_backgrounds=available_backgrounds)
    return render_template('admin_page.html', user=user, user_list=user_list)
  return redirect(url_for('dashboard'))

def admin_lvl_increase(user_id):
  admin = User.query.get(session['user_id'])
  if admin.admin_lvl == 2:
    user = User.query.get(user_id)
    user.admin_lvl = 2
    db.session.commit()
    return redirect(url_for('admin_page'))
  return redirect(url_for('dashboard'))

def admin_lvl_decrease(user_id):
  admin = User.query.get(session['user_id'])
  if admin.admin_lvl == 2:
      user = User.query.get(user_id)
      user.admin_lvl = 1
      db.session.commit()
      return redirect(url_for('admin_page'))
  return redirect(url_for('dashboard'))

def upload_background():
  admin = User.query.get(session['user_id'])
  if admin.admin_lvl == 2:
    if 'content' not in request.files:
      flash('No file part')
      return redirect(url_for('admin_page'))
    file = request.files['content']
    if file.filename == '':
      flash('No selected file')
      return redirect(url_for('admin_page'))
    if file and allowed_file(file.filename):
      filename = secure_filename(file.filename)
      file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
      filename = "images/" + secure_filename(file.filename)
      Background.create(title=request.form['title'], filename=filename)
      return redirect(url_for('admin_page'))
  return redirect(url_for('admin_page'))

def change_background():
  admin = User.query.get(session['user_id'])
  if admin.admin_lvl == 2:
    id = request.form['background']
    current = Background.query.filter_by(current = 1).all()
    for i in current:
      i.current = 0
      db.session.commit()
    new = Background.query.filter_by(id=id).first()
    new.current = 1
    db.session.commit()
    return redirect(url_for('admin_page'))
  return redirect(url_for('dashboard'))

def delete_user(user_id):
  admin = User.query.get(session['user_id'])
  if admin.admin_lvl == 2:
    user = User.query.get(user_id)
    db.session.delete(user)
    db.session.commit()
  return redirect(url_for('admin_page'))

def update_about_me():
  about_me = Post.query.get(1)
  admin = User.query.get(session['user_id'])
  if admin.admin_lvl == 2:
    about_me.text_content = request.form['text_content']
    db.session.commit()
  return redirect(url_for('about_me'))

def change_content_background():
  content_background = Post.query.get(2)
  admin = User.query.get(session['user_id'])
  if admin.admin_lvl == 2:
    content_background.text_content = request.form['text_content']
    db.session.commit()
  return redirect(url_for('dashboard'))