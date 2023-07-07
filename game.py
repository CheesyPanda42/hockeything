# Create a Game class with the following attributes:
# A rink
# A home team
# An away team
# A home team score
# An away team score
# A period
# A time
# The x,y coordinates of the puck
# The x,y coordinates of the home team players
# The x,y coordinates of the away team players

class Game:
    # Create a constructor with 3 parameters: rink, homeTeam, and awayTeam
    def __init__(self, rink, homeTeam, awayTeam):
        # Create 3 instance variables: rink, homeTeam, and awayTeam
        self.rink = rink
        self.homeTeam = homeTeam
        self.awayTeam = awayTeam

        # Create 2 instance variables: homeTeamScore and awayTeamScore
        self.homeTeamScore = 0
        self.awayTeamScore = 0

        # Create 2 instance variables: period and time
        self.period = 1
        self.time = 20

        # Create a tuple for puck coordinates
        self.puck = (50, 21)

        # Player coordinates are stored in a list of tuples
        # Create a list for home team player coordinates
        self.homeTeamPlayers = []
        # Create a list for away team player coordinates
        self.awayTeamPlayers = []

        # Create a for loop that will loop through the home team players
        for player in self.homeTeam.get_players():
            # Add the player's coordinates to the home team player coordinates list
            self.homeTeamPlayers.append((0,0))

        # Create a for loop that will loop through the away team players
        for player in self.awayTeam.get_players():
            # Add the player's coordinates to the away team player coordinates list
            self.awayTeamPlayers.append((0,0))

    # Create a method called get_rink that returns the game's rink
    def get_rink(self):
        return self.rink
    
