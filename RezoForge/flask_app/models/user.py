from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
class User:
    def __init__(self , data):
        self.id = data['id']
        self.name = data['name']
        self.username = data['username']
        self.email = data['email']
        self.location = data['location']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']


    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (name,username,email,location,age) VALUES (%(name)s,%(username)s,%(email)s,%(location)s,%(age)s)"
        return connectToMySQL('rezoforge_db').query_db(query,data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL('rezoforge_db').query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(user['username']) < 3:
            flash("Username must be at least 3 characters.")
            is_valid = False
        if len(user['email']) < 3:
            flash("Email must be at least 3 characters.")
            is_valid = False
        if len(user['location']) < 3:
            flash("Location must be at least 3 characters.")
            is_valid = False
        return is_valid
