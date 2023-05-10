from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DB, app
from flask_app.models import loginandreg



class Skeptic:
    def __init__(self , data ):
        self.id = data['id']
        self.name = data['name']
        self.num_of_sas = data['num_of_sas']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.skeptics = None

    
    @classmethod
    def delete_skeptic(cls, data):
        query  = "DELETE FROM sightings WHERE sightings.skeptic_id = %(id)s;"
        return connectToMySQL(DB).query_db(query, data)