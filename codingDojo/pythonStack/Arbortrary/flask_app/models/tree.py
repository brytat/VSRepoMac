from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Tree:
    db_name = "arbortrary_db"
    
    def __init__(self, db_data):
        self.id = db_data['id']
        self.species = db_data['species']
        self.location = db_data['location']
        self.reason = db_data['reason']
        self.date_planted = db_data['date_planted']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.user = None

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM trees JOIN users ON trees.user_id = users.id;"
        results = connectToMySQL(cls.db_name).query_db(query)
        trees = []
        for row in results:
            trees.append(cls(row))
        return trees

    @classmethod
    def get_one(cls, data):
        query = "SELECT trees.id, trees.species, trees.location, trees.date_planted, trees.reason, users.first_name AS first_name, users.last_name AS last_name FROM trees JOIN users ON trees.user_id = users.id WHERE trees.id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        tree = results[0]
        print(tree)
        return tree

    @classmethod
    def create_tree(cls, data):
        query = "INSERT INTO trees (species, location, reason, date_planted, created_at, updated_at, user_id) VALUES ( %(species)s, %(location)s, %(reason)s, %(date_planted)s, NOW(), NOW(), %(user_id)s );"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_trees_from_one_user(cls, data):
        query = "SELECT * FROM trees WHERE user_id = %(id)s;"
        trees_from_db = connectToMySQL(cls.db_name).query_db(query, data)
        trees = []
        for row in trees_from_db:
            trees.append( cls(row) )
        return trees
    
    # @classmethod
    # def all_trees_with_user(cls):
    #     query = "SELECT * FROM trees JOIN users ON trees.user_id = users.id;"
    #     trees_from_db = connectToMySQL(cls.db_name).query_db(query)
    #     print(trees_from_db)
    #     all_trees_instances = []
    #     for row_in_db in trees_from_db:
    #         tree_data = {
    #             'id': row_in_db["trees.id"],
    #             'species': row_in_db["species"],
    #             'location': row_in_db["location"],
    #             'reason': row_in_db["reason"],
    #             'date_planted': row_in_db["date_planted"],
    #             'created_at': row_in_db["trees.created_at"],
    #             'updared_at': row_in_db["trees.updated_at"],
    #         }
    #         user_data = {
    #             "id": row_in_db['id'],
    #             "first_name": row_in_db['first_name'],
    #             "last_name": row_in_db['last_name'],
    #             "email": row_in_db['email'],
    #             "password": row_in_db['password'],
    #             'created_at': row_in_db['first_name'],
    #             'updated_at': row_in_db['first_name']
    #         }
    #         tree_instance = cls(tree_data)
    #         user_instance = user.User(user_data)
    #         tree_instance.user = user_instance
    #         all_trees_instances.append(tree_instance)
    #     return all_trees_instances

    @classmethod
    def edit_tree(cls,data):
        query = "UPDATE trees SET species=%(species)s, location=%(location)s, reason=%(reason)s, date_planted=%(date_planted)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def delete_tree(cls,data):
        query  = "DELETE FROM trees WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @staticmethod
    def validate_tree(tree):
        is_valid = True
        if len(tree['species']) < 5:
            flash("Species must be at least 5 characters.")
            is_valid = False
        if len(tree['location']) < 2:
            flash("Location must be at least 2 characters.")
            is_valid = False
        if len(tree['reason']) > 50:
            flash("Reason must be 50 characters.")
            is_valid = False
        return is_valid