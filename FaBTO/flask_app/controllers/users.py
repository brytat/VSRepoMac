from flask import render_template, session, redirect, request

from flask_app import app
from flask_app.models.user import User
from flask_app.models.deck import Deck

@app.route('/user/<string:username>')
def render_user_page(username):
    pageName = "User Page"
    if "user_id" not in session:
        return redirect('/')
    data = {
        "user_id": session['user_id']
    }
    user = User.get_one(data)
    return render_template('userPage.html', pageName=pageName, user=user)