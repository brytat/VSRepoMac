from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.deck import Deck

@app.route('/deck/create', methods=['POST'])
def create_deck():
    if 'user_id' not in session:
        return redirect('/')
    data = {
        "deck_hero":request.form['deck_hero'],
        "format":request.form['format'],
        "deck_comp_level":request.form['deck_comp_level'],
        "description":request.form['description'],
        "user_id":request.form["user_id"]
    }
    print(data)
    Deck.create_deck(data)
    return redirect('/user/deck/<string:user_id>')

@app.route('/deck/edit/<int:deck_id>')
def render_edit_deck(deck_id):
    if 'user_id' not in session:
        return redirect('/')
    pageName = "Edit Deck"
    data = {
        'deck_id': deck_id
    }
    deck = Deck.get_one(data)
    deckhtml = deck[0]
    return render_template('editDeck.html', deck=deckhtml, pageName=pageName)

@app.route('/deck/update/<int:deck_id>', methods=['POST'])
def process_update_deck(deck_id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'deck_hero': request.form['deck_hero'],
        'format': request.form['format'],
        'deck_comp_level': request.form['deck_comp_level'],
        'description': request.form['description'],
        'deck_id': deck_id,
    }
    print(data)
    Deck.update_deck(data)
    return redirect('/user/deck/<string:user_id>')

@app.route('/deck/delete/<int:deck_id>')
def delete_deck(deck_id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'deck_id': deck_id
    }
    Deck.delete_deck(data)
    return redirect('/user/deck/<string:username>')