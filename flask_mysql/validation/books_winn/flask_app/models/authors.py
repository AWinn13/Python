from flask_app.config.mysqlconnection import connectToMySQL
from flask_app import DB, app
from flask_app.models import books

class Author:
    def __init__(self , data ):
        self.id = data['id']
        self.name = data['name']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.fav_books = []
        


    #--------------create----------------
    @classmethod
    def create_author(cls, data):
        query = "INSERT INTO authors (name) VALUES (%(name)s);" 
        return connectToMySQL(DB).query_db(query, data)
    
    #---------------get all----------------
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM authors;"
        
        results = connectToMySQL(DB).query_db(query)
        authors= []
        for i in results:
            authors.append(cls(i))
        return authors
    
    # -------------SELECT SINGLE USER--------------
    @classmethod
    def get_id(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        results = connectToMySQL(DB).query_db(query, data)
        if len(results) < 1:
            return False
        return cls(results[0])
    
    #--------------------CREATE FAVORITE-----------
    @classmethod
    def add_favorite(cls,data):
        query = "INSERT INTO favorites (author_id,book_id) VALUES (%(author_id)s,%(book_id)s);"
        return connectToMySQL('books').query_db(query,data)
    
    # ----------------------UNFAVORITE----------------

    @classmethod
    def unfavorited_authors(cls,data):
        query = "SELECT * FROM authors WHERE authors.id NOT IN ( SELECT author_id FROM favorites WHERE book_id = %(id)s );"
        authors = []
        results = connectToMySQL('books').query_db(query,data)
        for row in results:
            authors.append(cls(row))
        return authors
    # -------------------GET BY ID MANY TO MANY---------------------------------
    @classmethod
    def get_by_id(cls,data):
        query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON books.id = favorites.book_id WHERE authors.id = %(id)s;"
        results = connectToMySQL('books').query_db(query,data)

        # Creates instance of author object from row one
        author = cls(results[0])
        # append all book objects to the instances favorites list.
        for row in results:
            # if there are no favorites
            if row['books.id'] == None:
                break
            # common column names come back with specific tables attached
            data = {
                "id": row['books.id'],
                "title": row['title'],
                "pages": row['pages'],
                "created_at": row['books.created_at'],
                "updated_at": row['books.updated_at']
            }
            author.fav_books.append(books.Book(data))
        return author
    










#     @classmethod
#     def get_by_id(cls,data):
#         query = "SELECT * FROM authors LEFT JOIN favorites ON authors.id = favorites.author_id LEFT JOIN books ON books.id = favorites.book_id WHERE authors.id = %(id)s;"
#         results = connectToMySQL('books').query_db(query,data)

#         # Creates instance of author object from row one
#         author = cls(results[0])
#         # append all book objects to the instances favorites list.
#         for row in results:
#             # if there are no favorites
#             if row['books.id'] == None:
#                 break
#             # common column names come back with specific tables attached
#             data = {
#                 "id": row['books.id'],
#                 "title": row['title'],
#                 "num_of_pages": row['num_of_pages'],
#                 "created_at": row['books.created_at'],
#                 "updated_at": row['books.updated_at']
#             }
#             author.favorite_books.append(book.Book(data))
#         return author




# #!--------------USER validation--------------
#     @staticmethod
#     def validate_user(data):
#         is_valid = True
#         if len(data['first_name']) < 3:
#             flash("First name must be at least 3 characters.", 'reg_error')
#             is_valid = False
#         if len(data['last_name']) < 3:
#             flash("Last name must be at least 3 characters.", 'reg_error')
#             is_valid = False
#         if not EMAIL_REGEX.match(data['email']): 
#             flash(u"Invalid email address!", 'reg_error')
#             is_valid = False
#         if  User.get_email({ "email" : data["email"]}):
#             flash('Email already taken', 'reg_error')
#             is_valid = False
#         if not PASSWORD_REGEX.match(data['password']):
#             flash("password must be at least 8 characters and include 1 symbol !@#$%^&*()", 'reg_error')
#             is_valid = False
#         elif not data['password'] == data['confirm_password']:
#             flash("passwords don't match", 'reg_error')
#             is_valid = False
#         return is_valid
    

