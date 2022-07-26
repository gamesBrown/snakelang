
from flask_app.config.dbconnect import connectToMySQL

class Dojo:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.created = data["created"]
        self.updated = data["updated"]
        self.ninjas = []
    @classmethod
    def get_dojos(cls):
        query = "SELECT * from dojos"

            

        results = connectToMySQL("dojodb").query_db(query)
        dojos = []

        for dojo in results:
            dojos.append(cls(dojo))
        return dojos
    @classmethod
    def list_ninjas_in_single_dojo(cls,data):
        query = "SELECT * from dojos JOIN ninjas on dojo.id = ninjas.dojo_id WHERE dojos.id = %(id)s"

            

        results = connectToMySQL("dojodb").query_db(query,data)
        
        dojo_with_ninjas=cls(results[0])

        for entry in results:

            dojo_with_ninjas.ninjas.append=entry["username"]

            
        
        
        return dojo_with_ninjas

    @classmethod
    def dojo_create(cls,data):
        query = "INSERT INTO dojos (name,created,updated) VALUES(%(name)s,NOW(),NOW())"
                  

        return connectToMySQL("dojodb").query_db(query,data)
    
        

       