# This is the main file that will run the game
# This file will create the players and teams
# This file will also run the game

# Import the random module
import random

# Import the Player class from player.py
from player import Player

# Import the Team class from team.py
from team import Team

# Import the Rink class from rink.py
from rink import Rink

# Import the Game class from game.py
from game import Game

# Create an empty list called players
players = []

# Create a list of 10 names
names = ["Bob", "Joe", "Bill", "Tom", "Jim", "Tim", "Sam", "Max", "Ben", "Dan"]

# Create a list of 10 positions
positions = ["Center", "Left Wing", "Right Wing", "Defense", "Goalie"]

# Create a for loop that will loop 10 times
for i in range(10):
    # Create a random name
    name = random.choice(names)
    # Create a random position
    position = random.choice(positions)
    # Create a random stats list
    stats = []
    for i in range(5):
        stats.append(random.randint(1, 10))
    # Create a new player using the name, position, and stats
    player = Player(name, position, stats)
    # Add the player to the players list
    players.append(player)

# Print the player names and positions
for player in players:
    player.print_name_position()

# Create 2 teams
# Each team will have a random name, city, and 5 random players
# The teams will be stored in a list

# Create an empty list called teams
teams = []

# Create a list of 10 team names
team_names = ["Sharks", "Ducks", "Kings", "Coyotes", "Flames", "Oilers", "Canucks",]

# Create a list of 10 cities
cities = ["San Jose", "Anaheim", "Los Angeles", "Arizona", "Calgary", "Edmonton", "Vancouver"]

# Create a for loop that will loop 2 times
for i in range(2):
    # Create a random name
    name = random.choice(team_names)
    # Create a random city
    city = random.choice(cities)
    # Create a random players list
    team_players = []
    for i in range(5):
        team_players.append(random.choice(players))
    # Create a new team using the name, city, and players
    team = Team(name, city, team_players)
    # Add the team to the teams list
    teams.append(team)

# Print the team names
for team in teams:
    print(team.get_name())

# Create a rink
# The rink will have a random name, capacity, and 2 random teams
# The rink will be stored in a variable called rink

# Create a random name
rink_name = random.choice(team_names) + " Arena"
# Create a random capacity
rink_capacity = random.randint(10000, 20000)
# Create a random teams list
rink_teams = []
for i in range(2):
    rink_teams.append(random.choice(teams))

# Print the rink name
print(rink_name)

# Print the rink capacity
print(rink_capacity)

# Print the rink teams
for team in rink_teams:
    print(team.get_name())

# Create a rink using the name, capacity, and teams
rink = Rink(rink_name, rink_capacity, rink_teams)

rink.print_ice()

# Create a game
# The game will have a rink, 2 teams, and a score
# The game will be stored in a variable called game
game = Game(rink, rink_teams[0], rink_teams[1])

# Main game update loop
# Create an infinite loop to run the update logic
while True:
    rink.print_ice()
