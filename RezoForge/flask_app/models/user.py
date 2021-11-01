from flask_app.config.mysqlconnection import connectToMySQL

class User:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.username = data['username']
        self.location = data['location']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('rezoforge_db').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users