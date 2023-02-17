from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB

class Ninja:
    def __init__(self , data ):
        self.id = data['id']
        self.name = data['name']
        self.age = data['age']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']

    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema.
        results = connectToMySQL(DB).query_db(query)
        # Create an empty list to append our instances of users
        ninjas= []
        
        for i in results:
            ninjas.append(cls(i) )
        return ninjas

    @classmethod
    def create_ninja(cls, data):
        query = "INSERT INTO ninjas ( name , age , dojo_id ) VALUES (%(name)s, %(age)s, %(dojo_id)s);"
        return connectToMySQL(DB).query_db(query, data)