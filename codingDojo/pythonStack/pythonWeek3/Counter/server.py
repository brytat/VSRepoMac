from flask import Flask, render_template, redirect, session
app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"

@app.route('/')
def make_count():
    if "numHTML" not in session:
        session["numHTML"] = 0
    else:
        session["numHTML"] += 1
    return render_template("index.html")

@app.route('/destroy_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)