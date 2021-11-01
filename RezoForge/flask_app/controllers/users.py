from flask import render_template

from flask_app import app

from flask_app.models.user import User

@app.route('/')
def index():
    users = users.get_all()
    print(users)
    return render_template("frontpage/index.html", all_users = users)

@app.route('/user/<string:username>')
def hello(username):
    return render_template('userPage/index.html', userhtml=username)