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
    if not User.validate_user(request.form):
        return redirect('/signup')
    data = {
        "name_first":request.form['name_first'],
        "name_last":request.form['name_last'],
        "username":request.form['username'],
        "email":request.form['email'],
        "location_city":request.form['location_city'],
        "location_state":request.form['location_state'],
        "age":request.form['age']
    }
    User.save(data)
    return redirect('/')