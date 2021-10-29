from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)
app.secret_key = "keep it secret, keep it safe"

@app.route('/')
def new_index():
    return render_template("index.html")

@app.route('/process', methods=['POST'])
def process_form():


@app.route('/result')
def show_input():
    return render_template('display.html')

@app.route('/end_session')
def destroy():
    session.clear()
    return redirect('/')

if __name__=="__main__":
    app.run(debug=True)