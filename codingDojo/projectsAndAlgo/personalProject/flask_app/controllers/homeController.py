from flask import render_template, request, redirect, session

from flask_app import app
from flask_app.models.user import User
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

@app.route('/')
def homePage():
    pageName = "Front Page"
    print("User navigated to: " + pageName)
    return render_template("frontPage.html", pageName = pageName)

# @app.route('/user/<string:username>')
# def hello(username):
#     return render_template('userPage.html', userhtml=username)

@app.route('/signup')
def signup_form():
    pageName = "Sign up or sign in"
    return render_template('signUp.html', pageName = pageName)

@app.route('/create', methods=['POST'])
def create_user():
    if not User.validate_user(request.form):
        return redirect('/signup')
    pw_hash = bcrypt.generate_password_hash(request.form['password'])
    print(pw_hash)
    data = {
        "username":request.form['username'],
        "first_name":request.form['first_name'],
        "last_name":request.form['last_name'],
        "email":request.form['email'],
        "password":pw_hash
    }
    user_id = User.save_user_to_db(data)
    session['user_id'] = user_id
    return redirect('/')

@app.route('/login', methods=['POST'])
def process_login():
    data = {
        'username':request.form['username'],
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