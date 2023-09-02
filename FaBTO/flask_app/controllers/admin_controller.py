from flask import flash, url_for, render_template, request, redirect, session

from flask_app.controllers.users import render_user_page

from flask_app import app
from flask_app.models.admin import Admin
from flask_app.models.user import User
from flask_app.models.hub import Hub
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/admin/hero/heroDB/')
def render_admin(user):
    pageName = "Admin Hero Database"
    if "admin_id" not in session:
        return redirect('/')
    if user.admin == true:
        return redirect('/')
    return render_template('adminHeroDBPage.html', pageName=pageName, user=user)

@app.route('admin/hero/delete/<int:hero_id>')
def delete_hero():
    if session['user_id'] not in session:
        return redirect('/')
    if session['is_admin'] is False:
        return redirect('/')
    User.delete_hero_in_DB(data)
    return redirect('/admin/hero/heroDB')