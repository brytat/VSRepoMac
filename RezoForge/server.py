from flask import Flask, app, render_template
from user import User
app = Flask(__name__)
@app.route('/')
def index():
    users = User.get_all()
    print(users)
    return render_template("frontpage/index.html", all_users = users)

@app.route('/user/<string:username>/<int:num>')
def hello(user, num):
    return render_template('userPage/index.html', userhtml=user, numhtml=num)

if __name__ == "__main__":
    app.run(debug=True)