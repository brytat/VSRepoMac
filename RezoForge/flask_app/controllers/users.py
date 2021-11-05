from flask import render_template, request, redirect

from flask_app import app

from flask_app.models.user import User

@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("frontpage/index.html", all_users = users)

@app.route('/user/<string:username>')
def hello(username):
    return render_template('userPage/index.html', userhtml=username)

@app.route('/signup')
def signup_form():
    return render_template('signUp/index.html')

@app.route('/create', methods=['POST'])
def create_user():
    if not User.validate_burger(request.form):
        return redirect('/')
    User.save(request.form)