from flask import redirect, render_template, request
from flask_app import app
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/dojos')

@app.route("/dojos")
def show():
    dojos = Dojo.get_all()
    print(dojos)
    return render_template("dojos.html", all_dojos = dojos)

@app.route("/creatr/dojo", methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/dojos/<int:id>')
def show_dojo(id):
    data ={
        "id":id
    }
    print(id)
    return render_template("dojo_show.html", dojo = Dojo.get_dojo_with_ninjas(data))