from mysqlconnection import connectToMySQL
# model the class after the user table from our database
class User:
    def __init__( self , data ):
        self.id = data['id']
        self.first_name = data['first_name']
        self.last_name = data['last_name']
        self.email = data['email']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
    # use class methods to query database
    @classmethod
    def get_all(cls):
        query = "SELECT * FROM users;"
        # make sure to call the connectToMySQL function with the schema you are targeting.
        results = connectToMySQL('user_schema').query_db(query)
        # Create an empty list to append our instances of friends
        users = []
        # Iterate over the db results and create instances of friends with cls.
        for i in results:
            users.append( cls(i) )
        return users
    
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users (first_name,last_name,email) VALUES ( %(first_name)s,%(last_name)s,%(email)s);"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('user_schema').query_db( query, data )
    


# from mysqlconnection import connectToMySQL

# class User:
#     def __init__(self, data):
#         self.id = data['id']
#         self.first_name = data['first_name']
#         self.last_name = data['last_name']
#         self.email = data['email']
#         self.created_at = data['created_at']
#         self.updated_at = data['updated_at']

#     @classmethod
#     def get_all(cls):
#         query = "SELECT * FROM users;"
#         results = connectToMySQL('users_schema').query_db(query)
#         users = []
#         for u in results:
#             users.append( cls(u) )
#         return users

#     @classmethod
#     def save(cls, data):
#         query = "INSERT INTO users (first_name,last_name,email) VALUES (%(first_name)s,%(last_name)s,%(email)s);"

#         # comes back as the new row id
#         result = connectToMySQL('users_schema').query_db(query,data)
#         return result