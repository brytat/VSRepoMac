from flask import url_for, render_template, session, redirect, request

from flask_app import app
from flask_app.models.hub import Hub
from flask_app.models.deck import Deck
from flask_app.models.user import User

@app.route('/hub/login', methods=['POST'])
def process_hub_login():
    data = {
        'hub_un':request.form['hub_un'],
    }
    acceptable_id = Hub.validate_login(request.form, data)
    if acceptable_id == False:
        return redirect('/hub')
    session['hub_id'] = acceptable_id
    return redirect(url_for('render_hub_page', hub_id=session['hub_id']))

@app.route('/hub/<string:hub_un>')
def render_hub_page(hub):
    pageName = "Hub Page"
    if "hub_id" not in session:
        return redirect('/')
    data = {
        "hub_id": session['hub_id']
    }
    hub = Hub.get_one(data)
    return render_template('hubPage.html', pageName=pageName, hub=hub)


# Needs work need to properly call the hub info from path and check if user is in session and import the deck information of the user in session
@app.route('/hub/pits/<string:hub_un>')
def render_pits_page(hub):
    pageName = "Pits"
    if "user_id" not in session:
        return redirect('/')
    data = {
        "hub_id": session['hub_id']
    }
    dataUser = {
        "user_id": session['user_id']
    }
    user= User.get_one(dataUser)
    hub = Hub.get_one(data)
    return render_template('hubPitsPage.html', pageName=pageName, hub=hub, user=user)