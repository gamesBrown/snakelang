
from flask_app.config.dbconnect import connectToMySQL
from flask import flash
import re
class User:
    def __init__(self, data):
        self.idusers = data["idusers"]
        self.email = data["email"]
        self.password = data["password"]
        self.created_date = data["created_date"]
        self.updated_date = data["updated_date"]
       

    @staticmethod
    def validate_user(data):
        is_valid = True
        EMAIL_REGEX = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        if len(data["email"]) < 2 and len(data["email"]) > 255:
            flash("Your email is BOGUS")
            is_valid = False
        if data["password"] != data["confirm_password"]:
            flash("Your Passwords don't match you dingus")
            is_valid = False
        if not EMAIL_REGEX.match(data["email"]):
            flash("Please use da PROPA FO MAT for EMAIl")
            is_valid = False
        return is_valid

    @classmethod
    def login_with_email(cls,data):
        query = "SELECT * from users WHERE email=%(email)s"

        

        results = connectToMySQL("usersDB").query_db(query,data)
        

        if len(results)<1:
            return False
        return cls(results[0])

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
    def create_user(cls,data):
        query = "INSERT INTO users (email,password,updated_date,created_date) VALUES(%(email)s,%(password)s,NOW(),NOW())"
                  

        return connectToMySQL("usersDB").query_db(query,data)
        
    @classmethod
    def del_ninja(cls):
        pass

