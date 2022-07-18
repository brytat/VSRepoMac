from flask import render_template, session, redirect

from flask_app import app
from flask_app.models.user import User
from flask_app.models.deck import Deck

@app.route('/user/<string:user_id>')
def render_user_page(user_id):
    pageName = "User Page"
    #This needs tweaking to not have variable arg be determinate of session
    # if "user_id" not in session:
    #     return redirect('/')
    data = {
        "user_id": user_id
    }
    user = User.get_one(data)
    data1 = {
        "user_id": session['user_id']
    }
    session_user = User.get_one(data1)
    return render_template('userPage.html', pageName=pageName, user=user, session=session_user)

@app.route('/user/decks/<string:user_id>')
def render_decks_page(user_id):
    pageName = "User Page"
    if "user_id" not in session:
        return redirect('/')
    data = {
        "user_id": user_id
    }
    decks = Deck.get_decks_from_one_user(data)
    user = User.get_one(data)
    print(user)
    return render_template('displayDecks.html', pageName=pageName, user=user, decks=decks)