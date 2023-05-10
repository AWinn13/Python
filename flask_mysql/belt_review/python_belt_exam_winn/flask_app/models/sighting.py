from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DB, app
from flask_app.models import loginandreg
# from flask_app.models import skeptic



class Sighting:
    def __init__(self , data ):
        self.id = data['id']
        self.location = data['location']
        self.happened = data['happened']
        self.date = data['date']
        self.num_of_sas = data['num_of_sas']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.spotter = None
        # self.skeptics = None


    #-------------------Create-------------------------------------
    @classmethod
    def create_sighting(cls, data):
        query = "INSERT INTO sightings (location, happened, date, num_of_sas, user_id) VALUES (%(location)s, %(happened)s, %(date)s, %(num_of_sas)s, %(user_id)s);" 
        return connectToMySQL(DB).query_db(query, data)
    
    
    
    # -----------------------Update sighting-----------------------------------------
    @classmethod
    def update_sighting(cls, data):
        query = "UPDATE sightings SET location=%(location)s,happened=%(happened)s,num_of_sas=%(num_of_sas)s,date=%(date)s, user_id=%(user_id)s WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db( query, data )
    
    # @classmethod
    # def update_skeptic(cls, data):
    #     query = "UPDATE sightings SET skeptic_id = %(user_id)s WHERE id = %(id)s;"
    #     return connectToMySQL(DB).query_db( query, data )
    
    # --------------Delete------------------------------
    @classmethod
    def delete_sighting(cls, data):
        query  = "DELETE FROM sightings WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query, data)
    
    # @classmethod
    # def delete_skeptic(cls, data):
    #     query  = "UPDATE sightings SET skeptic_id = '' WHERE id = %(id)s;"
    #     return connectToMySQL(DB).query_db(query, data)
    
    # -----------------------Get all ONE TO MANY--------------------------
    
    @classmethod
    def get_all( cls ):
        query = "SELECT * FROM sightings join users on sightings.user_id = users.id;"
        results = connectToMySQL(DB).query_db(query)
        all_sightings = []
        if results:
            for row in results:
                # 
                this_sighting = cls(row)
                user_data= {
                    **row,
                    "id" : row["users.id"],
                    'created_at' : row['users.created_at'],
                    'updated_at' : row['users.updated_at']
                }

                
                this_user = loginandreg.User(user_data)
                this_sighting.spotter = this_user
                all_sightings.append(this_sighting)
        return all_sightings
    # -----------------------Get One ONE TO MANY-------------------------
    @classmethod
    def get_one_sighting(cls, data):
        query = "SELECT * FROM sightings JOIN users ON users.id = sightings.user_id WHERE sightings.id= %(id)s;"
        results = connectToMySQL(DB).query_db(query, data)
        if results:
            this_sighting = cls(results[0])
            row = results[0]
            user_data= {
                    **row,
                    "id" : row["users.id"],
                    'created_at' : row['users.created_at'],
                    'updated_at' : row['users.updated_at'],
                }
                
            # skeptic_data ={
            #         **row,
            #         'id' : row['skeptics.id'],
            #         'created_at' : row['skeptics.created_at'],
            #         'updated_at' : row['skeptics.updated_at']
            #     }

                
            # this_sighting.skeptics = skeptic.Skeptic(skeptic_data)
            this_user = loginandreg.User(user_data)
            this_sighting.spotter = this_user
            return this_sighting
        return this_sighting
    
    



    # ---------------------Validation-----------
    @staticmethod
    def validate_sighting(data):
        is_valid = True
        if len(data['location']) < 3:
            flash("location must be at least 3 characters.")
            is_valid = False
        if len(data['happened']) < 3:
            flash("happened must be at least 3 characters.")
            is_valid = False
        if len(data['num_of_sas']) < 1:
            flash("num_of_sass must be at least 1.")
            is_valid = False
        if len(data['date']) < 1:
            flash("Date cannot be blank.")
            is_valid = False
        return is_valid
