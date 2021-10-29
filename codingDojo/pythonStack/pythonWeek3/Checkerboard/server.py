from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def checkerboard():
    return render_template("index.html", num_rows=8, num_cols=8)

@app.route('/<int:rows>')
def custom_rows(rows):
    return render_template('index.html', num_rows=rows, num_cols=8)

@app.route('/<int:rows>/<int:cols>')
def custom_checkerboard(rows, cols):
    return render_template('index.html', num_rows=rows, num_cols=cols)

if __name__=="__main__":
    app.run(debug=True)