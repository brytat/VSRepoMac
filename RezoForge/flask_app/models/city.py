from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app

class City:
    db_name = "rezoforge_db"

    def __init__(self, data):
        self.id = data['id']
        #!!!getting a keyerror here!!!
        self.city_name = data['city_name']
        self.location_state_id = data['location_state_id']

    @classmethod
    def save_location_to_db(cls, data):
        query = "INSERT INTO location_cities (city_name, location_state_id,) VALUES (%(city_name)s,%(location_state_id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)