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
  backgrounds = Background.query.filter_by(current = 0).all()
  background = Background.query.filter_by(current = 1).first()
  if user.admin_lvl == 2:
      user_list = User.query.all()
      return render_template('admin_page.html', user=user, user_list=user_list, backgrounds=backgrounds, background=background)
  return redirect(url_for('dashboard'))

def admin_lvl_increase(user_id):
  admin = User.query.get(session['user_id'])
  if admin['admin_lvl'] == 2:
      user = User.query.get(user_id)
      user.admin_lvl_increase()
      return redirect(url_for('admin_page'))
  return redirect(url_for('dashboard'))

def admin_lvl_decrease(user_id):
  admin = User.query.get(session['user_id'])
  if admin['admin_lvl'] == 2:
      user = User.query.get(user_id)
      user.admin_lvl_decrease()
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
    current = Background.query.filter_by(current = 1)
    current.current = 0
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
