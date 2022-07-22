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
        print(query)
        return connectToMySQL(cls.db_name).query_db(query, data)


    #get data on one instance of a deck
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM decks JOIN users ON users.user_id = decks.user_id  WHERE deck_id = %(deck_id)s;"
        deck_from_db = connectToMySQL(cls.db_name).query_db(query, data)
        deck = deck_from_db
        print(deck)
        return deck
    
    @classmethod
    def get_decks_from_one_user(cls, data):
        query = "SELECT * FROM decks WHERE user_id = %(user_id)s;"
        decks_from_db = connectToMySQL(cls.db_name).query_db(query, data)
        decks = []
        if decks_from_db > 0:
            for row in decks_from_db:
                decks.append( cls(row) )
        print(decks)
        print(query)
        return decks

    @classmethod
    def update_deck(cls,data):
        query = "UPDATE decks SET deck_hero=%(deck_hero)s, format=%(format)s, deck_comp_level=%(deck_comp_level)s, description=%(description)s, updated_at=NOW() WHERE deck_id = %(deck_id)s;"
        print(query)
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def delete_deck(cls,data):
        query  = "DELETE FROM decks WHERE deck_id = %(deck_id)s;"
        print(query)
        return connectToMySQL(cls.db_name).query_db(query, data)
