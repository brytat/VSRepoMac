from nturl2path import url2pathname
from flask import render_template, session, redirect
import urllib.request, json

import os

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
    return render_template('User/userPage.html', pageName=pageName, user=user, session=session_user)

@app.route('/user/<string:user_id>/decks')
def render_decks_page(user_id):
    #Its about time i start using the API to get all the heroes 10.05.22
    url = "https://api.fabdb.net/cards?keywords=young".format(os.environ.get("73147f2ead15749ea59552e3940a6f9a9835eb861fd12052c1406a3897c7d9e9"))
    response = urllib.request.urlopen(url)
    data = response.read()
    dict =json.loads(data)
    #End of the API construction
    pageName = "User Page"
    if "user_id" not in session:
        return redirect('/')
    data = {
        "user_id": user_id
    }
    decks = Deck.get_decks_from_one_user(data)
    user = User.get_one(data)
    print(user)
    return render_template('User/displayDecks.html', pageName=pageName, user=user, decks=decks, heroes = dict["results"])

@app.route('/user/<string:user_id>/hubs')
def render_user_hubs_page(user_id):
    pageName = "User Hubs Page"
    if "user_id" not in session:
        return redirect('/')
    data = {
        "user_id": user_id
    }
    hubs = User.get_hubs_from_one_user(data)
    user = User.get_one(data)
    print(user)
    return render_template('User/displayUserHubs.html', pageName=pageName, user=user, hubs=hubs)