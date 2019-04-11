from flask import render_template, request, redirect, session, url_for, flash
from sqlalchemy import func
from server.models.posts import Post
from server.models.users import User
from server.models.backgrounds import Background

def admin_page():
  user = User.query.get(session['user_id'])
  if user['admin_lvl'] == 2:
      users = User.query.get().all()
      background = Background.query.filter_by(current=1)
      background = 
      return render_template(url_for('admin_page'), users=users)
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
    if admin['admin_lvl'] == 2:
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
        Background.create(filename=filename)
        return redirect(url_for('admin_page'))
  return redirect(url_for('dashboard'))

def switch_background():
  admin = User.query.get(session['user_id'])
    if admin['admin_lvl'] == 2:
      return redirect(url_for('admin_page'))