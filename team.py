# Stub for team class

# Create a class called Team
class Team:
    # Create a constructor with 3 parameters: name, city, and players
    def __init__(self, name, city, players):
        # Create 3 instance variables: name, city, and players
        self.name = name
        self.city = city
        self.players = players

    # Create a method called get_name that returns the team's name
    def get_name(self):
        return self.name
    
    # Create a method called get_players that returns the team's players
    def get_players(self):
        return self.players
    