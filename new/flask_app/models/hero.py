from flask_app.config.dbconnect import connectToMySQL

class Hero:
    def __init__(self, data):
        self.id = data["id"]
        self.name = data["name"]
        self.alter_ego = data["alter_ego"]
        self.power = data["power"]
        self.created = data["created"]
        self.updated = data["updated"]
    @classmethod
    def get_heroes(cls):
        query="SELECT * FROM heroes"

        result = connectToMySQL("superheroDB").query_db(query)

        heroes =[]

        for hero in result:
            heroes.append(cls(hero))
            return heroes
