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
    return redirect('/signup')

@app.route('/login', methods=['POST'])
def process_login():
    data = {
        'username':request.form['username']
    }
    user_in_db = User.get_by_username(data)
    acceptable_id = User.validate_login(request.form, data)
    if not user_in_db:
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
#GETTING AN ERROR HERE File "C:\Users\Bryton\.virtualenvs\FaBTO-v3ZnsrMK\Lib\site-packages\flask\app.py", line 2091, in __call__
# return self.wsgi_app(environ, start_response)
# File "C:\Users\Bryton\.virtualenvs\FaBTO-v3ZnsrMK\Lib\site-packages\flask\app.py", line 2076, in wsgi_app
# response = self.handle_exception(e)
# File "C:\Users\Bryton\.virtualenvs\FaBTO-v3ZnsrMK\Lib\site-packages\flask\app.py", line 2073, in wsgi_app
# response = self.full_dispatch_request()
# File "C:\Users\Bryton\.virtualenvs\FaBTO-v3ZnsrMK\Lib\site-packages\flask\app.py", line 1518, in full_dispatch_request
# rv = self.handle_user_exception(e)
# File "C:\Users\Bryton\.virtualenvs\FaBTO-v3ZnsrMK\Lib\site-packages\flask\app.py", line 1516, in full_dispatch_request
# rv = self.dispatch_request()
# File "C:\Users\Bryton\.virtualenvs\FaBTO-v3ZnsrMK\Lib\site-packages\flask\app.py", line 1502, in dispatch_request
# return self.ensure_sync(self.view_functions[rule.endpoint])(**req.view_args)
# File "F:\Users\Bryton\Documents\FaBTO\flask_app\controllers\homeController.py", line 54, in process_login
# return(url_for(render_user_page, user_id=4))
# File "C:\Users\Bryton\.virtualenvs\FaBTO-v3ZnsrMK\Lib\site-packages\flask\helpers.py", line 286, in url_for
# if endpoint[:1] == ".":
# TypeError: 'function' object is not subscriptable
    return(url_for(render_user_page))

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