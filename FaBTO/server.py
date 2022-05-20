from flask_app import app
from flask_app.controllers import homeController, users, decks, hubs

if __name__ == "__main__":
    app.run(debug=True)