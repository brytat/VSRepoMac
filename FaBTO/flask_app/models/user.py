from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

class User:
    db_name = "FaBTO"

    def __init__(self, data):
        self.user_id = data['user_id']
        self.username = data['username']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.password_hash = data['password_hash']
        self.is_admin=data['is_admin']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    #get data on one instance of a user
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE user_id = %(user_id)s;"
        user_from_db = connectToMySQL(cls.db_name).query_db(query, data)
        print("From model user.py print user_from_db result: %(user_from_db)s")
        if len(user_from_db) < 1:
            return False
        return cls(user_from_db[0])

    @classmethod
    def get_by_username(cls, data):
        query= "SELECT * FROM users WHERE username = %(username)s;"
        user_from_db = connectToMySQL(cls.db_name).query_db(query, data)
        print("From models user.py print get_by_username result: %(user_from_db)s")
        if len(user_from_db) < 1:
            return False
        else:
            return cls(user_from_db[0])

#This needs work. Need to validate that there are no duplicate cities entering in DB. Also need to add city.id to user.loction_city_id
    @classmethod
    def save_user_to_db(cls, data):
        query = "INSERT INTO users (username,first_name,last_name,email,password_hash) VALUES (%(username)s,%(first_name)s,%(last_name)s,%(email)s,%(password_hash)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)

    #search function needs to be created

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users ORDER BY users.username;"
        results = connectToMySQL(cls.db_name).query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    @classmethod
    def get_hubs_from_one_user(cls, data):
        #NEED TO COMPLETE QUERY WITH LEFT JOIN ON HUBS TO USERS
        query = "SELECT * FROM users WHERE user_id = %(username)s LEFT JOIN "
        results = connectToMySQL(cls.db_name).query_db(query)
        hubs = []
        for hub in results:
            hubs.append( cls(hub) )
        return hubs
    
    @classmethod
    def join_hub(cls, data):
        query = "INSERT INTO users_has_hubs (hub_id,user_id) VALUES (%(hub_id)s,%(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)
    
    @classmethod
    def leave_hub(cls, data):
        query  = "DELETE FROM users_has_hubs WHERE user_id = %(user_id)s && hub_id = %(hub_id)s;"
        print("MySQL query: %(query)s")
        return connectToMySQL(cls.db_name).query_db(query, data)

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['username']) < 3:
            flash("Username must be at least 3 characters.")
            is_valid = False
        if len(user['first_name']) < 3:
            flash("First name must be at least 3 characters.")
            is_valid = False
        if len(user['last_name']) < 3:
            flash("Last name must be at least 3 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address.")
            is_valid = False
        if user['password'] != user['confirm_password']:
            flash("Passwords do not match.")
            is_valid = False
        if len(user['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login(form_data, data_dictionary):
        is_valid = True
        query = "SELECT * FROM users WHERE username = %(username)s;"
        list_of_users = connectToMySQL(User.db_name).query_db(query, data_dictionary)
        print("From models user.py print var list_of_users: %(list_of_users)s")
        if len(list_of_users) < 1:
            is_valid = False
            flash("Invalid login credentials.")
        else:
            this_user = list_of_users[0]
            user_instance = User(this_user)
        if is_valid and not bcrypt.check_password_hash(user_instance.password_hash, form_data['password']):
            is_valid = False
            flash("Invalid login credentials.")
        if is_valid:
            is_valid = user_instance.user_id
        return is_valid
    
    @classmethod
    def delete_hero_in_DB(cls, data):
        query  = "DELETE FROM heroes WHERE hero_id = %(hero_id)s;"
        print("MySQL query: %(query)s")
        return connectToMySQL(cls.db_name).query_db(query, data)