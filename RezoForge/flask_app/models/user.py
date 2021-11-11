from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

class User:
    db_name = "rezoforge_db"

    def __init__(self , data):
        self.id = data['id']
        self.name_first = data['name_first']
        self.name_last = data['name_last']
        self.username = data['username']
        self.email = data['email']
        self.location_city = data['location_city']
        self.location_state = data['location_state']
        self.age = data['age']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def save(cls, data):
        query = "INSERT INTO users (name_first,name_last,username,email,location_city,location_state,age,password) VALUES (%(name_first)s,%(name_last)s,%(username)s,%(email)s,%(location_city)s,%(location_state)s,%(age)s,%(password)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)

    #search function not complete, need to define paramenter and parameter_argument
    # @classmethod
    # def search(cls, data):
    #     query = "SELECT * FROM users WHERE %(parameter)s = %(parameter_argument)s;"
    #     data = { 'parameter' : request.form['parameter_argument'] }
    #     result = mysql.query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db_name).query_db(query)
        users = []
        for user in results:
            users.append( cls(user) )
        return users

    @staticmethod
    def validate_user(user):
        is_valid = True
        if len(user['name_first']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(user['name_last']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(user['username']) < 3:
            flash("Username must be at least 3 characters.")
            is_valid = False
        if not EMAIL_REGEX.match(user['email']):
            flash("Invalid email address.")
            is_valid = False
        if len(user['location_city']) < 3:
            flash("City must be at least 3 characters")
            is_valid = False
        if len(user['location_state']) == 0:
            flash("Please select a state.")
            is_valid = False
        # if int(user['age']) < 13:
        #     flash("Must be 13 to join")
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
        query = "SELECT * FROM users WHERE email = %(email)s;"
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