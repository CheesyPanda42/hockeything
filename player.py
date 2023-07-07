# This file is a python class that represents a player in a hockey RPG game
# The class contains the player's name, position, and stats
# The class also contains methods to get and set the player's stats
# The class also contains a method to print the player's stats
# The class also contains a method to print the player's name and position



class Player:
    def __init__(self, name, position, stats):
        self.name = name
        self.position = position
        self.stats = stats

    def get_name(self):
        return self.name

    def get_position(self):
        return self.position

    def get_stats(self):
        return self.stats

    def set_name(self, name):
        self.name = name

    def set_position(self, position):
        self.position = position

    def set_stats(self, stats):
        self.stats = stats

    def print_stats(self):
        print(self.stats)

    def print_name_position(self):
        print(self.name + " " + self.position)    