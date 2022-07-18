from flask import url_for, render_template, request, redirect, session
from flask_app.controllers.users import render_user_page

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
        'username':request.form['username']
    }
    user_in_db = User.get_by_username(data)
    acceptable_id = User.validate_login(request.form, data)
    if not user_in_db:
<<<<<<< HEAD
        flash("Invalid login credentials.")
        print("user attempted to find a user not in DB")
        return redirect('/signup')
    # if acceptable_id == False:
    #     return redirect('/signup')
#Do We need to construct an elseif statement here???
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        flash("Invalid Email/Password")
        print("User entered an incorrect password for " + user_in_db.username)
        return redirect('/signup')
    # if the passwords matched,
    session['user_id'] = user_in_db.user_id
    return redirect('/user/<string:username>')
=======
        # flash("Invalid login credentials.")
        return redirect('/signup')
    if acceptable_id == False:
        return redirect('/signup')
    if not bcrypt.check_password_hash(user_in_db.password, request.form['password']):
        # if we get False after checking the password
        # flash("Invalid Email/Password")
        return redirect('/signup')
    # if the passwords matched
    session['user_id'] = acceptable_id
    return(redirect(url_for('render_user_page', user_id=acceptable_id)))
>>>>>>> ee49c6006e0e114b3ffd2bba2ed3cce813bb599e

@app.route('/signup')
def signup_form():
    pageName = "Sign up or sign in"
    return render_template('signUp.html', pageName = pageName)

@app.route('/hub/signup')
def signup_form_hub():
    pageName = "Hub sign up or sign in"
    return render_template('hubSignUp.html', pageName = pageName)

@app.route("/logout")
def log_out():
    session.clear()
    return redirect("/")