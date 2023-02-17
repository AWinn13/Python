from flask_app.config.mysqlconnection import connectToMySQL
from flask_app.models import ninja 
from flask_app import DB
class Dojo:
    def __init__(self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        self.ninjas = []


    ##*******Iterate over the db results and create instances of dojos with cls.*******
    @classmethod
    def get_all_dojos(cls):
        query = "SELECT * FROM dojos;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DB).query_db(query)
        # Create an empty list to append our instances of users
        dojos= []
        
        for i in results:
            dojos.append(cls(i) )
        return dojos


    #--------------Create a new dojo----------------
    @classmethod
    def create(cls, data):
        query = "INSERT INTO dojos (name) VALUES (%(name)s);"
        return connectToMySQL(DB).query_db(query, data)
    
    # --------------Join the 
    @classmethod
    def get_ninjas_and_dojos( cls , data ):
        query = "SELECT * FROM dojos JOIN ninjas ON ninjas.dojo_id = dojos.id WHERE dojos.id = %(id)s;"
        results = connectToMySQL(DB).query_db(query , data)
        if results:
        # creating instance of dojo
            dojo = cls(results[0])
            for one_ninja in results:
                # 
                ninja_data = {
                    "id" : one_ninja["id"],
                    "name" : one_ninja["ninjas.name"],
                    "age" : one_ninja["age"],
                    "created_at" : one_ninja["created_at"],
                    "updated_at" : one_ninja["updated_at"],
                    "dojo_id" : one_ninja["dojo_id"]
                }
                dojo.ninjas.append(ninja.Ninja( ninja_data ))
            return dojo
        return False
    
    

    
