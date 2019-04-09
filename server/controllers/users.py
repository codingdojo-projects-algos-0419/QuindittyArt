from flask import render_template, request, redirect, session, url_for, flash
from sqlalchemy import func
from server.models.quotes import Quote
from server.models.users import User

def new():
    return render_template('Log_and_reg.html')

def create():
    errors = User.validate(request.form)
    if errors:
        for error in errors:
            flash(error)
        return redirect(url_for('users:new'))
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
    return redirect(url_for("users:new"))

def users_quotes(user_id):
    user = User.query.get(user_id)
    quotes = Quote.query.filter_by(user_id=user_id)
    possesive = "'"
    if user.last_name[len(user.last_name)-1] != 's':
        possesive = "'s"
    return render_template('users_quotes.html', user=user, quotes=quotes, possesive=possesive)

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
    user.first_name = request.form['first_name']
    user.last_name = request.form['last_name']
    user.email = request.form['email']
    db.session.commit()
    return redirect(url_for('dashboard'))

def admin_page():
    user = session['user_id']
    if user.admin_lvl == 2:
        users = User.query.get().all()
    return redirect(url_for('dashboard'))


def admin_lvl_increase(user_id):
    user = User.query.get(user_id)
    user.admin_lvl_increase()
    return redirect(url_for('admin_page'))