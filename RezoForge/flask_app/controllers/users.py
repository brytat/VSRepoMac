from flask import render_template, request, redirect, session
from flask_app import app
from flask_app.models.user import User
from flask_app_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("frontpage.html", all_users = users)

@app.route('/user/<string:username>')
def hello(username):
    return render_template('userPage.html', userhtml=username)

@app.route('/signup')
def signup_form():
    return render_template('signUp.html')

@app.route('/create', methods=['POST'])
def create_user():
    if not User.validate_user(request.form):
        return redirect('/signup')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "name_first":request.form['name_first'],
        "name_last":request.form['name_last'],
        "username":request.form['username'],
        "email":request.form['email'],
        "location_city":request.form['location_city'],
        "location_state":request.form['location_state'],
        "age":request.form['age'],
        "password":pw_hash
    }
    user_id = User.save(data)
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