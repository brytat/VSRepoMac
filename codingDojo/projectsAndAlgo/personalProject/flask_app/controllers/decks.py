from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.user import User

@app.route('/deck/create', methods=['POST'])
def create_deck():
    pass

@app.route('/deck/update/<int:deck_id>')
def render_update_deck(deck_id):
    pass

@app.route('/deck/delete/<int:deck_id>')
def delete_deck(deck_id):
    pass