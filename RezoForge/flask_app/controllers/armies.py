from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.user import User
from flask_app.models.tree import Tree

@app.route('/new/tree')
def new_tree():
    user = session['user_id']
    return render_template('new_tree/index.html', user = user)

#render Edit Tree Page
@app.route('/edit/<int:id>')
def edit_tree_page(id):
    if "user_id" not in session:
        return redirect('/')
    data1 = {
        'id':session['user_id']
    }
    user = User.get_one(data1)
    data2 = {
        "id":id
    }
    tree = Tree.get_one(data2)
    return render_template('edit_tree/index.html', user=user, tree = tree)

#process Edit (POST)
@app.route('/edit/tree/<int:id>', methods=['POST'])
def edit_tree(id):
    if 'user_id' not in session:
        return redirect('/')
    if not Tree.validate_tree(request.form):
        return redirect('/edit/'+str(id))
    data = {
        'species': request.form['species'],
        'location': request.form['location'],
        'reason': request.form['reason'],
        'date_planted': request.form['date_planted'],
        'id': id
    }
    Tree.edit_tree(data)
    return redirect('/user/account')

#route for adding tree to DB (POST)
@app.route('/new/create/tree', methods=['POST'])
def create_new_tree():
    if 'user_id' not in session:
            return redirect('/')
    if not Tree.validate_tree(request.form):
        return redirect('/new/tree')
    data = {
        'species': request.form['species'],
        'location': request.form['location'],
        'reason': request.form['reason'],
        'date_planted': request.form['date_planted'],
        'user_id': session['user_id']
    }
    print(data)
    Tree.create_tree(data)
    return redirect('/dashboard')

@app.route('/show/<int:id>')
def render_show(id):
    print(session['user_id'])
    data1 = {
        'id':session['user_id']
    }
    user = User.get_one(data1)
    data2 = {
        "id":id
    }
    tree = Tree.get_one(data2)
    return render_template('show_tree/index.html', user=user, tree=tree)

@app.route("/user/account")
def render_user_trees():
    if "user_id" not in session:
        return redirect('/')
    data = {
        'id':session['user_id']
    }
    user = User.get_one(data)
    all_trees = Tree.get_trees_from_one_user(data)
    return render_template('account/index.html', user=user,trees=all_trees)

#route for deleting a tree (POST)
@app.route('/trees/<int:id>/delete')
def delete_tree(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': id
    }
    Tree.delete_tree(data)
    return redirect('/user/account')