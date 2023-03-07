# -----------------WORKED WITH PEYTON--------------

from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DB, app
from flask_app.models import loginandreg
from datetime import datetime


class Recipe:
    def __init__(self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instruction = data['instruction']
        self.date = data['date']
        self.underthirty = data['underthirty']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.user_id = data['user_id']
        self.maker = None


    #-------------------Create-------------------------------------
    @classmethod
    def create_recipe(cls, data):
        query = "INSERT INTO recipes (name, description, instruction, date, underthirty, user_id) VALUES (%(name)s, %(description)s, %(instruction)s, %(date)s, %(underthirty)s, %(user_id)s);" 
        return connectToMySQL(DB).query_db(query, data)
    
    
    # @classmethod
    # def get_all_recipe(cls):
    #     query = "SELECT recipes.name, recipes.underthirty, users.first_name  FROM recipes join users on recipes.user_id = users.id;"
    #     return connectToMySQL(DB).query_db(query)
    
    # -----------------------Update recipe-----------------------------------------
    @classmethod
    def update(cls, data):
        query = "UPDATE recipe SET name=%(name)s,description=%(description)s,instruction=%(instruction)s,date=%(date)s,underthirty=%(underthirty)s WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db( query, data )
    
    # --------------Delete------------------------------
    @classmethod
    def delete(cls, data):
        query  = "DELETE FROM recipes WHERE id = %(id)s;"
        return connectToMySQL(DB).query_db(query, data)
    
    # -----------------------Get all--------------------------
    @classmethod
    def get_recipes_and_users( cls ):
        query = "SELECT * FROM recipes join users on recipes.user_id = users.id;"
        results = connectToMySQL(DB).query_db(query)
        print(results)
        all_recipes = []
        if results:
            for row in results:
                # 
                this_recipe = cls(row)
                user_data= {
                    **row,
                    "id" : row["users.id"],
                    'created_at' : row['users.created_at'],
                    'updated_at' : row['users.updated_at']
                }
                this_user = loginandreg.User(user_data)
                this_recipe.maker = this_user
                all_recipes.append(this_recipe)
        return all_recipes
    # -----------------------Get One-------------------------
    @classmethod
    def get_one_recipe(cls, data):
        query = "SELECT * FROM recipes LEFT JOIN users ON users.id = recipes.user_id WHERE recipes.id= %(id)s;"
        results = connectToMySQL(DB).query_db(query, data)
        if results:
            this_recipe = cls(results[0])
            row = results[0]
            user_data= {
                    **row,
                    "id" : row["users.id"],
                    'created_at' : row['users.created_at'],
                    'updated_at' : row['users.updated_at'],
                }
                
            this_user = loginandreg.User(user_data)
            this_recipe.maker = this_user
            return this_recipe
        return False



    # ---------------------Validation-----------
    @staticmethod
    def validate_recipe(data):
        is_valid = True
        if len(data['name']) < 3:
            flash("Name must be at least 3 characters.")
            is_valid = False
        if len(data['description']) < 3:
            flash("description must be at least 3 characters.")
            is_valid = False
        if len(data['instruction']) < 3:
            flash("Instructions must be at least 3 characters.")
            is_valid = False
        if len(data['date']) < 1:
            flash("Date cannot be blank.")
            is_valid = False
        if 'underthirty' not in data:
            flash("Must specify if recipe is under 30 minutes.")
            is_valid = False
        return is_valid
