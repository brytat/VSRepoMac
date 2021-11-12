from flask import render_template, request, redirect, session
# from flask.ext.session import Session
from werkzeug.exceptions import TooManyRequests
from flask_app import app
from flask_app.models.user import User
from flask_app.models.tree import Tree
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
# Session(app)

# render front page
@app.route('/')
def login_registration_page():
    if "user_id" in session:
        return redirect('/dashboard')
    return render_template("register_login/index.html")

#process user creation
@app.route('/register', methods=['POST'])
def register_user():
    #if parameters are not valid send back to registration page
    if not User.validate_registration(request.form):
        return redirect('/')
    data = {
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "email":request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password']),
    }
    User.create_user(data)
    session['user_id'] = User.get_one_by_email(data).id
    print(session['user_id'])
    return redirect('/dashboard')

#process session creation
@app.route('/login', methods=['POST'])
def process_login():
    data = {
        'email':request.form['email'],
    }
    acceptable_id = User.validate_login(request.form, data)
    if acceptable_id == False:
        return redirect('/')
    session['user_id'] = User.get_one_by_email(data).id
    print(session['user_id'])
    return redirect('/dashboard')

#render user page
@app.route('/dashboard')
def user_page():
    if "user_id" not in session:
        return redirect('/')
    data = {
        "id": session['user_id']
    }
    user = User.get_one(data)
    all_trees= Tree.get_all()
    print(all_trees)
    return render_template('dashboard/index.html', user=user, trees=all_trees)

#end session
@app.route("/logout")
def log_out():
    session.clear()
    return redirect("/")
