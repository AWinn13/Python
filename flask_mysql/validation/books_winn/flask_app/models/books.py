# -----------------WORKED WITH PEYTON

from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DB, app
from datetime import datetime
from flask_app.models import authors


class Book:
    def __init__(self , data ):
        self.id = data['id']
        self.title = data['title']
        self.pages = data['pages']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.authors_fav = []
        self.authors_who_fav = []


    #-------------------Create-------------------------------------
    @classmethod
    def create(cls, data):
        query = "INSERT INTO books (title, pages ) VALUES (%(title)s, %(pages)s);" 
        return connectToMySQL(DB).query_db(query, data)
    
    
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM books;"
        results = connectToMySQL(DB).query_db(query)
        books= []
        for i in results:
            books.append(cls(i))
        return books
    

    @classmethod
    def get_by_id( cls, data ):
        query = "SELECT * FROM books LEFT JOIN favorites on books.id=favorites.book_id LEFT JOIN authors on authors.id = favorites.author_id WHERE books.id = %(id)s;"
        results = connectToMySQL(DB).query_db(query, data)
        
        if results:
            for row in results:
                if row['authors.id'] == None:
                    break
                data= {
                    **row,
                    "id" : row["authors.id"],
                    'created_at' : row['authors.created_at'],
                    'updated_at' : row['authors.updated_at']
                }
                book = cls(results[0])
                book.authors_fav.append(authors.Author(data))
            return book
        return False
    

    @classmethod
    def unfavorited_books(cls,data):
        query = "SELECT * FROM books WHERE books.id NOT IN ( SELECT book_id FROM favorites WHERE author_id = %(id)s );"
        results = connectToMySQL('books').query_db(query,data)
        books = []
        for row in results:
            books.append(cls(row))
        print(books)
        return books
    









    @classmethod
    def get_by_id2(cls,data):
        query = "SELECT * FROM books LEFT JOIN favorites ON books.id = favorites.book_id LEFT JOIN authors ON authors.id = favorites.author_id WHERE books.id = %(id)s;"
        results = connectToMySQL('books').query_db(query,data)

        book = cls(results[0])

        for row in results:
            if row['authors.id'] == None:
                break
            data = {
                "id": row['authors.id'],
                "name": row['name'],
                "created_at": row['authors.created_at'],
                "updated_at": row['authors.updated_at']
            }
            book.authors_who_fav.append(authors.Author(data))
        return book


    
    # -----------------------Update recipe-----------------------------------------
    # @classmethod
    # def update(cls, data):
    #     query = "UPDATE recipe SET name=%(name)s,description=%(description)s,instruction=%(instruction)s,date=%(date)s,underthirty=%(underthirty)s WHERE id = %(id)s;"
    #     return connectToMySQL(DB).query_db( query, data )
    
    # # --------------Delete------------------------------
    # @classmethod
    # def delete(cls, data):
    #     query  = "DELETE FROM recipes WHERE id = %(id)s;"
    #     return connectToMySQL(DB).query_db(query, data)
    
    # # -----------------------Get all--------------------------
    # @classmethod
    # def get_recipes_and_users( cls ):
    #     query = "SELECT * FROM recipes join users on recipes.user_id = users.id;"
    #     results = connectToMySQL(DB).query_db(query)
    #     print(results)
    #     all_recipes = []
    #     if results:
    #         for row in results:
    #             # 
    #             this_recipe = cls(row)
    #             user_data= {
    #                 **row,
    #                 "id" : row["users.id"],
    #                 'created_at' : row['users.created_at'],
    #                 'updated_at' : row['users.updated_at']
    #             }
    #             this_user = loginandreg.User(user_data)
    #             this_recipe.maker = this_user
    #             all_recipes.append(this_recipe)
    #         return all_recipes
    #     return False
    # # -----------------------Get One-------------------------
    # @classmethod
    # def get_one_recipe(cls, data):
    #     query = "SELECT * FROM recipes LEFT JOIN users ON users.id = recipes.user_id WHERE recipes.id= %(id)s;"
    #     results = connectToMySQL(DB).query_db(query, data)
    #     if results:
    #         this_recipe = cls(results[0])
    #         row = results[0]
    #         user_data= {
    #                 **row,
    #                 "id" : row["users.id"],
    #                 'created_at' : row['users.created_at'],
    #                 'updated_at' : row['users.updated_at'],
    #             }
                
    #         this_user = loginandreg.User(user_data)
    #         this_recipe.maker = this_user
    #         return this_recipe
    #     return False



    # # ---------------------Validation-----------
    # @staticmethod
    # def validate_recipe(data):
    #     is_valid = True
    #     if len(data['name']) < 3:
    #         flash("Name must be at least 3 characters.")
    #         is_valid = False
    #     if len(data['description']) < 3:
    #         flash("description must be at least 3 characters.")
    #         is_valid = False
    #     if len(data['instruction']) < 3:
    #         flash("Instructions must be at least 3 characters.")
    #         is_valid = False
    #     if len(data['date']) < 1:
    #         flash("Date cannot be blank.")
    #         is_valid = False
    #     if 'underthirty' not in data:
    #         flash("Must specify if recipe is under 30 minutes.")
    #         is_valid = False
    #     return is_valid
