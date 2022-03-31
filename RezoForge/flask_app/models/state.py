from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import app

class State:
    db_name = "rezoforge_db"

    def __init__(self, data):
        self.id = data['id']
        #!!!getting a keyerror here!!!
        self.state_code = data['state_code']
        self.state_name = data['state_name']

    @classmethod
    def get_info_states(cls):
        query = "SELECT * FROM location_states;"
        results = connectToMySQL(cls.db_name).query_db(query)
        states = []
        for state in results:
            states.append( cls(state) )
        return states