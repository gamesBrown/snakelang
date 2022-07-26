from flask_app.config.dbconnect import connectToMySQL
from flask import flash
from flask_app.models.users import User
import re
class Recipe:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.description = data["description"]
        self.instructions = data["instructions"]
        self.under30 = data["under30"]
        self.created_date = data["created_date"]
        self.updated_date = data["updated_date"]
        self.user_id = data["user_id"]
        self.poster=None

       

    @staticmethod
    def validate_recipe(data):
        pass
        
        

    @classmethod
    def login_with_email(cls,data):
        query = "SELECT * from users WHERE email=%(email)s"

        

        results = connectToMySQL("recipeDB").query_db(query,data)
        

        if len(results)<1:
            return False
        return cls(results[0])

    @classmethod
    def get_recipes(cls):
        query = "SELECT * from recipes JOIN recipeDB.users ON recipeDB.users.id = user_id"

        

        results = connectToMySQL("recipeDB").query_db(query)
        recipes = []

        for recipe in results:
            this_recipe = cls(recipe)
            poster = {
            "id":recipe["users.id"],
            "first_name":recipe["first_name"],
            "last_name":recipe["last_name"],
            "email":recipe["email"],
            "password":None,
            "created_date":recipe["created_date"],
            "updated_date":recipe["updated_date"],
            
            
        }
            this_recipe.poster=User(poster)
            recipes.append(this_recipe)
            
        return recipes
    @classmethod
    def get_one_recipe_by_id(cls, data):
        query = "SELECT * from recipes WHERE id=%(id)s"


        results = connectToMySQL("recipeDB").query_db(query, data)

        if len(results) < 1:
            return False
        return cls(results[0])
    @classmethod
    def display_recipe_with_poster(cls, data):
        query = "SELECT * from recipes JOIN recipeDB.users ON recipeDB.users.id = user_id WHERE recipes.id=%(id)s"

        # SELECT * from recipes
        # JOIN recipeDB.users ON recipeDB.users.id = user_id
        # WHERE recipes.user_id = 5

        
        results = connectToMySQL("recipeDB").query_db(query, data)
      
        for item in results:
            recipe = Recipe(item)
            poster = {
            "id":item["users.id"],
            "first_name":item["first_name"],
            "last_name":item["last_name"],
            "email":item["email"],
            "password":None,
            "created_date":item["created_date"],
            "updated_date":item["updated_date"],
            
            
        }
        recipe.poster=User(poster)
        
        # recipe.poster = User(poster)
        
        if len(results) < 1:
            return False
        return recipe

    @classmethod
    def create_recipe(cls,data):
        query = "INSERT INTO recipes (name,description,instructions,under30,updated_date,created_date,user_id) VALUES(%(name)s,%(description)s,%(instructions)s,%(under30)s,NOW(),NOW(),%(user_id)s)"
                  

        return connectToMySQL("recipeDB").query_db(query,data)
    @classmethod
    def edit_recipe(cls,data):
        query = "UPDATE recipes SET name=%(name)s,description=%(description)s,instructions=%(instructions)s,under30=%(under30)s,updated_date=NOW() WHERE id=%(id)s"
                  

        return connectToMySQL("recipeDB").query_db(query,data)
        
        
    @classmethod
    def del_recipe(cls,data):
        query = "DELETE FROM recipes WHERE id=%(id)s;"

        return connectToMySQL("recipeDB").query_db(query,data)

