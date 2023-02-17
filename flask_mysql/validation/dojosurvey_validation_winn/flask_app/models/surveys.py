from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash

from flask_app import DB
class Survey:
    def __init__(self , data ):
        self.id = data['id']
        self.name = data['name']
        self.animal = data['animal']
        self.food = data['food']
        self.location = data['location']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        
        


    ##*******Iterate over the db results and create instances of dojos with cls.*******
    @classmethod
    def get_all_results(cls):
        query = "SELECT * FROM surveys;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL(DB).query_db(query)
        # Create an empty list to append our instances of users
        surveys= []
        
        for i in results:
            surveys.append(cls(i) )
        return surveys


    #--------------survey results----------------
    @classmethod
    def create(cls, data):
        query = "INSERT INTO surveys (name, animal, food, location) VALUES (%(name)s, %(animal)s, %(food)s, %(location)s);"
        return connectToMySQL(DB).query_db(query, data)
    
    @classmethod
    def get_survey(cls):
        query = "SELECT * FROM surveys ORDER BY surveys.id DESC LIMIT 1;"
        results = connectToMySQL(DB).query_db(query)
        return Survey(results[0])

    
    @staticmethod
    def validate_survey(survey):
        is_valid = True # we assume this is true
        if len(survey['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(survey['animal']) < 3:
            flash("Animal must be at least 3 characters.")
            is_valid = False
        if len(survey['food']) < 3:
            flash("Food must be pizza.")
            is_valid = False
        if len(survey['location']) < 1:
            flash("Ya gotta choose a location.")
            is_valid = False
        return is_valid
