from flask import Flask, redirect, render_template, request
# import the class from users.py
from user import User
app = Flask(__name__)
@app.route("/users")
def index():
    # call the get all classmethod to get all friends
    users = User.get_all()
    print(users)
    return render_template("read.html", all_users = users)
            
@app.route("/users/new")
def render_create_new():
    return render_template("create.html")

@app.route("/users/process", methods=['POST'])
def process_form():
    data = {
        'first_name': request.form['first_name'],
        'last_name': request.form['last_name'],
        'email': request.form['email']
    }
    User.save(data)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)