from flask_app import render_template, redirect, session

from flask_app import app
from flask_app.models.hero import Hero

@app.route('/admin/hero/heroDB/')
def render_admin_heroDB_page(user):
    pageName = "Admin Hero Database"
    if session['user_id'] not in session:
        return redirect('/')
    if session['admin'] == False:
        return redirect('/denied')
    return render_template('adminHeroDBPage.html', pageName=pageName, user=user)

@app.route('admin/hero/update_list')
def update_hero_list():
    if session['user_id'] not in session:
        return redirect('/')
    if session['is_admin'] == False:
        return redirect('/denied')
    Hero.update_hero_list()
    return redirect('admin/hero/heroDB')

@app.route('admin/hero/delete/<int:hero_id>')
def delete_hero(hero_id):
    if session['user_id'] not in session:
        return redirect('/')
    if session['is_admin'] == False:
        return redirect('/denied')
    data = {
        "hero_id" : hero_id
    }
    Hero.delete_hero_in_DB(data)
    return redirect('/admin/hero/heroDB')