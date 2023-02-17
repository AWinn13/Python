from mysqlconnection import connectToMySQL
# model the class after the user table from our database ----responsible for creating the table and inserting data into it
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
        # Create an empty list to append our instances of users
        users = []
        #*******Iterate over the db results and create instances of users with cls.*******
        for i in results:
            users.append( cls(i) )
        return users
    
    #class method to query database
    @classmethod
    def save(cls, data ):
        query = "INSERT INTO users (first_name,last_name,email) VALUES ( %(first_name)s,%(last_name)s,%(email)s);"
        # data is a dictionary that will be passed into the save method from server.py
        return connectToMySQL('user_schema').query_db( query, data )
    
    #class method to update database
    @classmethod
    def update(cls, data):
        query = "UPDATE users SET first_name=%(first_name)s,last_name=%(last_name)s,email=%(email)s WHERE id = %(id)s;"

        return connectToMySQL('user_schema').query_db( query, data )
    
    # class method to delete user from database
    @classmethod
    def delete(cls, user_id):
        query  = "DELETE FROM users WHERE id = %(id)s;"
        data = {"id": user_id}
        return connectToMySQL('user_schema').query_db(query, data)
    
    # class method to display single user
    @classmethod
    def show_single_user(cls, data):
        query = "SELECT * FROM users WHERE id = %(id)s;"
        result = connectToMySQL('user_schema').query_db(query, data)
        if result:
            return cls(result[0]) 
        return False
    



