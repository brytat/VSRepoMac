from flask import Flask, render_template
from flask.templating import render_template_string  # Import Flask to allow us to create our app
app = Flask(__name__)    # Create a new instance of the Flask class called "app"
app.secret_key = "keep it secret, keep it safe"
@app.route('/')          # The "@" decorator associates this route with the function immediately following
def index():
    return render_template("index.html")  # Return the string 'Hello World!' as a response

@app.route('/hello/<string:fruit>/<int:num>')
def hello(fruit, num):
    return render_template('hello.html', fruithtml=fruit, numhtml=num)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.