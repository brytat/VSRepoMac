from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.user import User
from flask_app.models.deck import Deck

@app.route('/deck/create', methods=['POST'])
def create_deck():
    if 'user_id' not in session:
        return redirect('/')
    username : session["username"]
    data = {
        "deck_hero":request.form['deck_hero'],
        "format":request.form['format'],
        "deck_comp_level":request.form['deck_comp_level'],
        "description":request.form['description'],
        "user_id":request.form["user_id"]
    }
    print(data)
    Deck.create_deck(data)
    return redirect('/user/deck/<string:username>')

@app.route('/deck/update/<int:deck_id>')
def render_update_deck(deck_id):
    pass

@app.route('/deck/delete/<int:deck_id>')
def delete_deck(deck_id):
    pass