from flask import Flask, redirect, render_template, request
# import the class from users.py
from user import User

app = Flask(__name__)

@app.route('/')
def index():
    return redirect('/users')

@app.route("/users")
def users():
    users = User.get_all()
    print(users)
    return render_template("read(all).html", all_users = users)
            
@app.route("/user/new")
def new():
    return render_template("create.html")

@app.route("/user/process", methods=['POST'])
def process_form():
    User.save(request.form)
    return redirect('/users')

@app.route('/user/edit/<int:id>')
def render_edit(id):
    data ={
        "id":id
    }
    print(id)
    return render_template("edituser.html", one_user = User.get_one(data))

@app.route('/user/show/<int:id>')
def show(id):
    data ={ 
        "id":id
    }
    return render_template("read(one).html", user = User.get_one(data))

@app.route('/user/update',methods=['POST'])
def update():
    User.update(request.form)
    return redirect('/users')

@app.route('/user/destroy/<int:id>')
def destroy(id):
    data ={
        'id':id
    }
    User.destroy(data)
    return redirect('/users')

if __name__ == "__main__":
    app.run(debug=True)