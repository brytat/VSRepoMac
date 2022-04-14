from flask_app import app
from flask_app.controllers import homeController
from flask_app.controllers import users
from flask_app.controllers import decks

if __name__ == "__main__":
    app.run(debug=True)