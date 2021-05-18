from flask_app.config.mysqlconnection import connectToMySQL
from .ninja import Ninja


class Dojo :
    def __init__(self,data):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.ninjas = []

    @classmethod
    def new_dojo(cls, data):
        query = "INSERT INTO dojos (name, created_at, updated_at) VALUES (%(name)s, NOW(), NOW());"
        return connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        dojos = []
        for x in results:
            dojos.append(cls(x))
        return dojos

    @classmethod
    def get_dojo_by_id(cls,data):
        query = "SELECT FROM dojos WHERE id = %(id)s"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query,data)
        dojo_obj = cls(results[0])

        return dojo_obj

    @classmethod
    def get_ninjas_in_dojo(cls, data):
        query = "SELECT * FROM ninjas WHERE dojo_id = %(id)s;"
        results = connectToMySQL("dojos_and_ninjas_schema").query_db(query)
        
        dojo = cls(results[0])
        
        for row in results:
            data = {
                "id": row['ninjas.id'],
                "dojo_id" : row['dojo_id'],
                "first_name" : row['first_name'],
                "last_name" : row['last_name'],
                "age" : row['age'],
                "created_at" : ['ninjas.created_at'],
                "updated_at" : ['ninjas.updated_at']
            }
            dojo.ninjas.append(Ninja(data))
        
        return dojo