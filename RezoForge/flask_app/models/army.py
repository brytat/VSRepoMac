from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app.models import user

class Tree:
    db_name = "rezoforge_db"
    
    def __init__(self, db_data):
        self.id = db_data['id']
        self.faction = db_data['faction']
        self.points_total = db_data['points_total']
        self.name = db_data['name']
        self.comp_level = db_data['comp_level']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.user = None

    @classmethod
    def get_all(cls):
        query = "SELECT * FROM armies JOIN users ON armies.user_id = users.id;"
        results = connectToMySQL(cls.db_name).query_db(query)
        trees = []
        for row in results:
            trees.append(cls(row))
        return trees

    @classmethod
    def get_one(cls, data):
        query = "SELECT * FROM armies JOIN users ON armies.user_id = users.id WHERE armies.id = %(id)s;"
        results = connectToMySQL(cls.db_name).query_db(query, data)
        army = results[0]
        print(army)
        return army

    @classmethod
    def create_army(cls, data):
        query = "INSERT INTO armies (faction, points_total, name, comp_level, created_at, updated_at, user_id) VALUES (%(faction)s, %(points_total)s, %(name)s, %(comp_level)s, NOW(), NOW(), %(user_id)s);"
        return connectToMySQL(cls.db_name).query_db(query, data)

    @classmethod
    def get_armies_from_user(cls, data):
        query = "SELECT * FROM armies WHERE user_id = %(id)s;"
        armies_from_db = connectToMySQL(cls.db_name).query_db(query, data)
        armies = []
        for row_from_db in armies_from_db:
            army_data = {
                'id':row_from_db['id'],
                'faction':row_from_db['faction'],
                'points_total':row_from_db['points_total'],
                'name':row_from_db['name'],
                'comp_level':row_from_db['comp_level'],
                'created_at':row_from_db['created_at'],
                'updated_at':row_from_db['updated_at']
                
            }
            armies.append(army_data)
        return armies
    
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
    def edit_army(cls,data):
        pass
        query = "UPDATE trees SET species=%(species)s, location=%(location)s, reason=%(reason)s, date_planted=%(date_planted)s, updated_at=NOW() WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query,data)

    @classmethod
    def delete_army(cls,data):
        query  = "DELETE FROM armies WHERE id = %(id)s;"
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @staticmethod
    def validate_army(army):
        is_valid = True
        if len(army['species']) < 5:
            flash("Species must be at least 5 characters.")
            is_valid = False
        if len(army['location']) < 2:
            flash("Location must be at least 2 characters.")
            is_valid = False
        if len(army['reason']) > 50:
            flash("Reason must be 50 characters.")
            is_valid = False
        return is_valid