
from flask_app.config.dbconnect import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.username = data["username"]
        self.password = data["password"]
        self.email = data["email"]
        self.created = data["created"]
        self.updated = data["updated"]
        self.dojo_id = data["dojo_id"]

    @classmethod
    def get_ninjas(cls):
        query = "SELECT * from ninjas"

        

        results = connectToMySQL("dojodb").query_db(query)
        ninjas = []

        for ninja in results:
            ninjas.append(cls(ninja))
        return ninjas
    @classmethod
    def get_ninja(cls):
        pass
    @classmethod
    def create_ninja(cls,data):
        query = "INSERT INTO ninjas (username,password,email,created,updated,dojo_id) VALUES(%(username)s,%(password)s,%(email)s,NOW(),NOW(),7)"
                  

        return connectToMySQL("dojodb").query_db(query,data)
        
    @classmethod
    def del_ninja(cls):
        pass




