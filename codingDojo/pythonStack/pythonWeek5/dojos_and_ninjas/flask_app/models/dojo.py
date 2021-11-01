from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja

class Dojo:
    def __init__(self, db_data):
        self.id = db_data['id']
        self.name = db_data['name']
        self.created_at = db_data['created_at']
        self.updated_at = db_data['updated_at']
        self.ninjas = []

    @classmethod
    def save(cls, data):
        query = "INSERT INTO dojos (name, created_at, Updated_at) VALUES ( %(name)s, NOW(), NOW() );"
        return connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)

    @classmethod
    def get_dojo_with_ninjas(cls, data):
        query = "SELECT * FROM dojos LEFT JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL('dojos_and_ninjas_schema').query_db(query, data)
        dojo = cls(results[0])
        for row_from_db in results:
            ninja_data = {
                "id" : row_from_db['ninjas.id'],
                "first_name" : row_from_db['ninjas.first_name'],
                "last_name" : row_from_db['ninjas.last_name'],
                "age" : row_from_db['ninjas.age'],
                "created_at" : row_from_db['ninjas.created_at'],
                "updated_at" : row_from_db['ninjas.updated_at']
            }
            dojo.ninjas.append( ninja.Ninja( ninja_data ) )
        return dojo

    # @classmethod
    # def get_one(cls, data ):
    #     query  = "SELECT * FROM dojos WHERE id = %(id)s";
    #     result = connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)
    #     return cls(result[0])

    # @classmethod
    # def update(cls,data):
    #     query = "UPDATE dojos SET name=%(name)s, updated_at=NOW() WHERE id = %(id)s;"
    #     return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)

    # @classmethod
    # def destroy(cls,data):
    #     query  = "DELETE FROM dojos WHERE id = %(id)s;"
    #     return connectToMySQL('dojos_and_ninjas_schema').query_db(query,data)