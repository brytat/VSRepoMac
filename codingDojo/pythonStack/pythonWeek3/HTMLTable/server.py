from flask import Flask, render_template

app = Flask(__name__)    # Create a new instance of the Flask class called "app"

app.secret_key = "keep it secret, keep it safe"

@app.route('/users')
def render_users():
    user_info = [
        {'first_name' : 'Michael', 'last_name' : 'Choi'},
        {'first_name' : 'John', 'last_name' : 'Supsupin'},
        {'first_name' : 'Mark', 'last_name' : 'Guillen'},
        {'first_name' : 'KB', 'last_name' : 'Tonel'}
    ]
    return render_template("index.html", users=user_info)

if __name__=="__main__":   # Ensure this file is being run directly and not from a different module    
    app.run(debug=True)    # Run the app in debug mode.