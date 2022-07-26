from flask_app.config.dbconnect import connectToMySQL

class Ninja:
    def __init__(self, data):
        self.id = data["id"]
        self.username = data["username"]
        self.password = data["passwrod"] 
        self.email = data["email"]
        self.created = data["created"]
        self.updated = data["updated"]
        self.dojo_id = data["dojo_id"]

    @classmethod
    def get_ninjas(cls):
        query="SELECT * FROM ninjas"

        result = connectToMySQL("dojoDB").query_db(query)

        ninjas=[]

        for ninja in result:
            ninjas.append(cls(ninja))
        return ninjas

    @classmethod
    def insert_ninja(cls,data):
        data = {

        }
        query="INSERT INTO dojoDB.ninjas(username, password, email, NOW(), NOW(), dojo_id) VALUES ( %(username)s , %(password)s , %(email)s , NOW() , NOW() %(dojo_id)s);"

        return connectToMySQL("dojoDB").query_db(query,data)