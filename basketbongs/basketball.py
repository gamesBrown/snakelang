class Player:
    @classmethod
    def get_team(cls,players)
        
    def __init__(self, player_dict):
        self.name = player_dict['name']
        self.age = player_dict['age']
        self.position = player_dict['position']
        self.team = player_dict['team']

kevin = {
    	"name": "Kevin Durant", 
    	"age":34, 
    	"position": "small forward", 
    	"team": "Brooklyn Nets"
}
jason = {
    	"name": "Jason Tatum", 
    	"age":24, 
    	"position": "small forward", 
    	"team": "Boston Celtics"
}
kyrie = {
    	"name": "Kyrie Irving", 
    	"age":32,
        "position": "Point Guard", 
    	"team": "Brooklyn Nets"
}
    
# Create your Player instances here!
# player_jason = ???



team1 =[]

player_list = []

player_kyrie = Player(kyrie)
player_jason = Player(jason)
player_kevin = Player(kevin)


team1.append(player_kyrie)
team1.append(player_jason)
team1.append(player_kevin)

player_list.append(kyrie)
player_list.append(jason)
player_list.append(kevin)

for player in team1:
    print(player.name)

