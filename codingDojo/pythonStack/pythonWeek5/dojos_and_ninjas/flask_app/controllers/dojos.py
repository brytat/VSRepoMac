from flask import redirect, render_template
from werkzeug.exceptions import RequestURITooLarge

from flask_app import app

from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route("/dojos")
def show():
    dojos = Dojo.get_dojo_with_ninjas()
    print(dojos)
    return render_template("dojos.html", all_dojos = dojos)
            
@app.route("/ninjas")
def new():
    dojos = Dojo.get_all()
    return render_template("new_ninja.html", all_dojos = dojos)

# @app.route('/dojos/<int:id>')
# def render_edit(id):
#     data ={
#         "id":id
#     }
#     print(id)
#     return render_template("dojo_show.html", Dojo = Dojo.get_one(data))