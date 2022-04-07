from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

class User:
    db_name = "rezoforge_db"

    def __init__(self, data):
        self.id = data['id']
        #!!!getting a keyerror here!!!
        self.username = data['username']
        self.name_first = data['name_first']
        self.name_last = data['name_last']
        self.email = data['email']
        self.location_city_id = data['location_city_id']
        #dont need this will most likely remove
        #self.location_state = data['location_state']
        self.age = data['age']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

#This needs work. Need to validate that there are no duplicate cities entering in DB. Also need to add city.id to user.loction_city_id
    @classmethod
    def save_user_to_db(cls, data):
        query = "INSERT INTO users (username, name_first,name_last,email, location_city_id,age,password) VALUES (%(username)s,%(name_first)s,%(name_last)s,%(email)s,%(location_city_id)s,%(age)s,%(password)s);"
        #Add this to query if needed to create location cities
        # INSERT INTO location_cities (city_name, location_state_id) VALUES (%(city_name)s,%(location_state_id)s;
        return connectToMySQL(cls.db_name).query_db(query,data)

    #search function needs to be created

    @classmethod
    def get_all_users(cls):
        query = "SELECT * FROM users LEFT JOIN location_cities ON users.location_city_id = location_cities.id LEFT JOIN location_states ON location_cities.location_state_id = location_states.id ORDER BY users.name_first;"
        results = connectToMySQL(cls.db_name).query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    @staticmethod
    def validate_user(user):
        is_valid = True
        #NEEDS WORK needs to validate that username is unique
        if len(user['username']) < 3:
            flash("Username must be at least 3 characters.")
            is_valid = False
        if len(user['name_first']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(user['name_last']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address.")
            is_valid = False
        #THIS NEEDS WORK need to make this a not null validation
        # if len(user['location_city_id']) < 3:
        #     flash("City must be at least 3 characters")
        #     is_valid = False
        # if len(user['location_state']) == 0:
        #     flash("Please select a state.")
        #     is_valid = False
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
        if len(list_of_users) < 1:
            is_valid = False
            flash("Invalid login credentials.")
        this_user = list_of_users[0]
        user_instance = User(this_user)
        if is_valid and not bcrypt.check_password_hash(user_instance.password, form_data['password']):
            is_valid = False
            flash("Invalid login credentials.")
        if is_valid:
            is_valid = user_instance.id
        return is_valid