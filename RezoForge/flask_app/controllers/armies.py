from flask import render_template, redirect, request, session
from flask_app import app
from flask_app.models.user import User
from flask_app.models.army import Army

@app.route('/new/army')
def new_army():
    user = session['user_id']
    return render_template('new_army.html', user = user)

#render Edit Army Page
@app.route('/edit/<int:id>')
def edit_army_page(id):
    if "user_id" not in session:
        return redirect('/')
    data1 = {
        'id':session['user_id']
    }
    user = User.get_one(data1)
    data2 = {
        "id":id
    }
    army = Army.get_one(data2)
    return render_template('edit_army.html', user=user, army = army)

#process Edit (POST)
@app.route('/edit/army/<int:id>', methods=['POST'])
def edit_army(id):
    if 'user_id' not in session:
        return redirect('/')
    if not Army.validate_army(request.form):
        return redirect('/edit/'+str(id))
    data = {
        'faction': request.form['faction'],
        'points_total': request.form['points_total'],
        'name': request.form['name'],
        'comp_level': request.form['comp_level'],
        'id': id
    }
    Army.edit_army(data)
    return redirect('/user/account')

#route for adding tree to DB (POST)
@app.route('/new/create/army', methods=['POST'])
def create_new_tree():
    if 'user_id' not in session:
            return redirect('/')
    if not Army.validate_army(request.form):
        return redirect('/new/army')
    data = {
        'faction': request.form['faction'],
        'points_total': request.form['points_total'],
        'name': request.form['name'],
        'comp_level': request.form['comp_level'],
        'id': id
    }
    print(data)
    Army.create_army(data)
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
    army = Army.get_one(data2)
    return render_template('show_army.html', user=user, army=army)

@app.route("/user/account")
def render_user_trees():
    if "user_id" not in session:
        return redirect('/')
    data = {
        'id':session['user_id']
    }
    user = User.get_one(data)
    all_armies = Army.get_armies_from_one_user(data)
    return render_template('account.html', user=user,armies=all_armies)

#route for deleting an army (POST)
@app.route('/army/<int:id>/delete')
def delete_army(id):
    if 'user_id' not in session:
        return redirect('/')
    data = {
        'id': id
    }
    Army.delete_army(data)
    return redirect('/user/account')