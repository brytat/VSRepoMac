from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL

class Deck:
    db_name="FaBTO"