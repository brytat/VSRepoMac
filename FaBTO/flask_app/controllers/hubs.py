from flask import url_for, render_template, session, redirect, request

from flask_app import app
from flask_app.models.hub import Hub
from flask_app.models.deck import Deck

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

@app.route('/hub/<string:hub_id>')
def render_hub_page(hub):
    pageName = "Hub Page"
    if "hub_id" not in session:
        return redirect('/')
    data = {
        "hub_id": session['hub_id']
    }
    hub = Hub.get_one(data)
    return render_template('hubPage.html', pageName=pageName, hub=hub)