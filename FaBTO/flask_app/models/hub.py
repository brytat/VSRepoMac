from flask_app import app
import re
from flask_app.config.mysqlconnection import connectToMySQL
from flask_bcrypt import Bcrypt
bcrypt = Bcrypt(app)
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]+$')
from flask import flash
class Hub:
    db_name="FaBTO"

    def __init__(self, data):
        self.hub_id = data['hub_id']
        self.hub_name = data['hub_name']
        self.hub_email = data['hub_email']
        self.hub_location = data['hub_location']
        self.hub_desription = data['hub_description']
        self.password = data['password']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM hubs WHERE hub_id = %(hub_id)s;"
        hub_from_db = connectToMySQL(cls.db_name).query_db(query, data)
        if len(hub_from_db) < 1:
            return False
        return cls(hub_from_db[0])

    @classmethod
    def save_hub_to_db(cls, data):
        query = "INSERT INTO hubs (hub_name,hub_email,hub_location,hub_description,hub_password) VALUES (%(hub_name)s,%(hub_email)s,%(hub_location)s,%(hub_description)s,%(hub_password)s);"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def getAllMembersOfHub(cls, data):
        query = "SELECT * FROM users_has_hubs WHERE hub_id = %(hub_id)s JOIN users WHERE user_id = user_id;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @staticmethod
    def validate_hub(hub):
        is_valid = True
        if not EMAIL_REGEX.match(hub['email']):
            flash("Invalid email address.")
            is_valid = False
        if hub['password'] != hub['confirm_password']:
            flash("Passwords do not match.")
            is_valid = False
        if len(hub['password']) < 8:
            flash("Password must be at least 8 characters.")
            is_valid = False
        return is_valid

    @staticmethod
    def validate_login_hub(form_data, data_dictionary):
        is_valid = True
        query = "SELECT * FROM hubs WHERE hub_name = %(hub_name)s;"
        list_of_hubs = connectToMySQL(Hub.db_name).query_db(query, data_dictionary)
        if len(list_of_hubs) < 1:
            is_valid = False
            flash("Invalid login credentials.")
        this_hub = list_of_hubs[0]
        hub_instance = Hub(this_hub)
        if is_valid and not bcrypt.check_password_hash(hub_instance.password, form_data['password']):
            is_valid = False
            flash("Invalid login credentials.")
        if is_valid:
            is_valid = hub_instance.hub_id
        return is_valid