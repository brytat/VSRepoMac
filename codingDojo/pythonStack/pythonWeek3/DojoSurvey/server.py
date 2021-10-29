from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"

@app.route('/')
def new_index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process_form():
    session['user_name'] = request.form['name']
    session['user_location'] = request.form['location']
    session['user_language'] = request.form['language']
    session['user_comment'] = request.form['comment']
    return redirect('/result')

@app.route('/result')
def show_input():
    return render_template('display.html')

@app.route('/end_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)