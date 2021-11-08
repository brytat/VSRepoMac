from flask_app import app
from flask import render_template, request, redirect, session
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def login_registration_page():
    if "user_id" in session:
        return redirect('/dashboard')
    return render_template("signUp/index.html")

@app.route('/register', methods=['POST'])
def register_user():
    if not User.validate_registration(request.form):
        return redirect('/')
    data = {
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "email":request.form['email'],
        "password": bcrypt.generate_password_hash(request.form['password']),
    }
    session['user_id'] = User.create_user(data)
    return redirect('/dashboard')

@app.route('/login', methods=['POST'])
def process_login():
    data = {
        'email':request.form['email'],
    }
    acceptable_id = User.validate_login(request.form, data)
    if acceptable_id == False:
        return redirect('/')
    session['user_id'] = acceptable_id
    return redirect('/dashboard')

@app.route('/dashboard')
def user_page():
    if "user_id" not in session:
        return redirect('/')
    data = {
        "id": session['user_id'],
        #"password": bcrypt.generate_password_hash(request.form['password']),
    }
    this_user = User.get_one(data)
    return render_template('userPage/index.html', userhtml=this_user)

@app.route("/logout")
def log_out():
    session.clear()
    return redirect("/")