from flask_app.config.mysqlconnection import connectToMySQL
from flask import flash
from flask_app import DB, app
from flask_app.models import loginandreg



class Skeptic:
    def __init__(self , data ):
        self.id = data['id'],
        self.user_id = data['user_id'],
        self.user_id = data['sighting_id']


    @classmethod
    def count_all(cls, data):
        query = " SELECT COUNT(skeptics.user_id) AS count from sightings join skeptics on sightings.id=skeptics.sighting_id where sightings.id = %(sighting_id)s;"
        return connectToMySQL(DB).query_db(query, data)


    # @classmethod
    # def delete_skeptic(cls, data):
    #     query  = "DELETE FROM sightings WHERE sightings.skeptic_id = %(id)s;"
    #     return connectToMySQL(DB).query_db(query, data)