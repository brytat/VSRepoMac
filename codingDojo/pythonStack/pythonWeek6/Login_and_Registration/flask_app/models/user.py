from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
import re
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')
from flask_app import app
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)

class User:
    db_name = "login_db"

    def __init__(self , data):
        self.id = data['id']
        self.name_first = data['first_name']
        self.name_last = data['last_name']
        self.email = data['email']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def create_user(cls, data):
        query = "INSERT INTO users (first_name, last_name, email, passsword) VALUES (%(first_name)s, %(last_name)s, %(email)s, %(password)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        results = connectToMySQL(cls.db).query_db(query)
        users = []
        for row in results:
            users.append( cls(row))
        return users
        
    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM users WHERE email = %(email)s;"
        user_from_db = connectToMySQL(cls.db_name).query_db(query, data)
        if len(user_from_db) < 1:
            return False
        return cls(user_from_db[0])

    @staticmethod
    def validate_registration(user):
        is_valid = True
        if len(user['first_name']) < 2:
            flash("Name must be at least 2 characters.")
            is_valid = False
        if len(user['last_name']) < 2:
            flash("Name must be at least 2 characters.")
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
