from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL

class Deck:
    db_name="FaBTO"

    def __init__(self, data):
        self.deck_id = data['deck_id']
        self.deck_hero = data['deck_hero']
        self.format = data['format']
        self.deck_comp_level = data['deck_comp_level']
        self.description = data['description']
        self.user_id = data['user_id']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_deck(cls, data):
        query = "INSERT INTO decks (deck_hero, format, deck_comp_level, description, user_id) VALUES ( %(deck_hero)s, %(format)s, %(deck_comp_level)s, %(description)s, %(user_id)s );"
        return connectToMySQL(cls.db_name).query_db(query, data)


    #get data on one instance of a deck
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM decks WHERE deck_id = %(deck_id)s JOIN users ON decks.user_id = users.user_id;"
        deck_from_db = connectToMySQL(cls.db_name).query_db(query, data)
        if len(deck_from_db) < 1:
            return False
        return cls(deck_from_db[0])
    
    @classmethod
    def get_decks_from_one_user(cls, data):
        query = "SELECT * FROM decks WHERE user_id = %(user_id)s;"
        decks_from_db = connectToMySQL(cls.db_name).query_db(query, data)
        decks = []
        for row in decks_from_db:
            decks.append( cls(row) )
        return decks
