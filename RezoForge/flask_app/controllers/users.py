from flask import render_template, request, redirect, session

from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    users = User.get_all_users()
    print(users)
    return render_template("frontPage.html", all_users = users)

@app.route('/user/<string:username>')
def hello(username):
    return render_template('userPage.html', userhtml=username)

@app.route('/signup')
def signup_form():
    form_info_states = User.get_info_states()
    return render_template('signUp.html', location_states=form_info_states)

@app.route('/create', methods=['POST'])
def create_user():
    if not User.validate_user(request.form):
        return redirect('/signup')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "username":request.form['username'],
        "name_first":request.form['name_first'],
        "name_last":request.form['name_last'],
        "email":request.form['email'],
        "age":request.form['age'],
        "location_city":request.form['location_city'],
        "location_state":request.form['location_state'],
        "password":pw_hash
    }
    user_id = User.save_user_to_db(data)
    session['user_id'] = user_id
    return redirect('/')

@app.route('/login', methods=['POST'])
def process_login():
    data = {
        'email':request.form['email'],
    }
    acceptable_id = User.validate_login(request.form, data)
    if acceptable_id == False:
        return redirect('/')
    session['user_id'] = acceptable_id
    return redirect('/user/<string:username>')

@app.route("/logout")
def log_out():
    session.clear()
    return redirect("/")