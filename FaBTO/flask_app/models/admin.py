from flask_app import app
from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models.user import User

class Admin:
    @classmethod
    def delete_hero_in_DB(cls, data):
        query = "DELETE FROM heroes WHERE hero_id = %(hero_id)s;"
        print("MySQL query: %(query)s")
        return connectToMySQL(cls.db_name).query_db(query, data)
    
    @classmethod
    def update_hero_list(cls):
        query1 = "DROP heroes;"
        connectToMySQL(cls.db_name).query_db(query1)
        url = "https://api.fabdb.net/cards/?keywords=hero&keywords=young".format(os.environ.get("73147f2ead15749ea59552e3940a6f9a9835eb861fd12052c1406a3897c7d9e9"))
        response = urllib.request.urlopen(url)
        data1 = response.read()
        dict = json.loads(data1)
        print(dict)
        listHeroes = []
        for x in dict:
            listHeroes.append(dict['data'][x]['name'])
        print(listHeroes)
        for x in listHeroes:
            query2 = "INSERT INTO heroes (hero_name) VALUES (%(x)s);"
            connectToMySQL(cls.db_name).query_db(query2)
        return listHeroes
