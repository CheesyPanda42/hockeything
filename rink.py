# This file creates a class that represents a rink in a hockey RPG game
# The class contains the rink's name, capacity, and teams
# The class also contains methods to get and set the rink's name, capacity, and teams
# The ice is 200 feet long and 85 feet wide. It is represented by a 2D list that breaks the ice into 5x5 foot squares
# The ice is represented by a 2D list that is 40x17
# Each square on the ice is represented by a "-" character
# A home team player is represented by a "H" character
# An away team player is represented by an "A" character
# The puck is represented by a "*" character. If a player has the puck, the puck will be in the same square as the player
# A player with the puck will be represented by "H*" or "A*" as appropriate
# Goalies are represented by "HG" or "AG" as appropriate
# The goal is represented by "[]"
# The centerline is represented by "||"
# The blue lines are represented by "|"
# The goal lines are represented by "="

class Rink:
    def __init__(self, name, capacity, teams):
        # Create 3 instance variables: name, capacity, and teams
        self.name = name
        self.capacity = capacity
        self.teams = teams
        # Create a 2D list that represents the ice
        # The ice is 200 feet long and 85 feet wide. There are the following markings on the ice:
        # The centerline divides the ice in half
        # The blue lines are 25 feet from the centerline
        # The goal lines are 11 feet from the end of the ice
        # The goal is 6 feet wide
    
        # Each square on the ice is 2x2 feet
        # The ice is represented by a 2D list that is 102x44
        # Each square on the ice is represented by a "   " string
        # The ice is surrounded by boards, represented by 2 lines of "#" characters

        self.ice = []
        for i in range(44):
            row = []
            for j in range(101):
                row.append("   ")
            self.ice.append(row)

        # Draw the outline of a circle in the center of the ice, diameter 25 feet, using '-' characters
        # The center of the circle is at (50, 21)

        for i in range(44):
            for j in range(101):
                if (i-21)**2 + (j-50)**2 > 94 and (i-21)**2 + (j-50)**2 < 106:
                    self.ice[i][j] = " . "
        
        # Add the centerline and blue lines
        for i in range(44):
            self.ice[i][50] = " || "
            self.ice[i][25] = " + "
            self.ice[i][75] = " + "
        # Add the goal lines
        for i in range(44):
            self.ice[i][5] = " | "
            self.ice[i][95] = " | "

        # Add the goals
        for i in range(6):
            self.ice[19+i][5] = " @ "
            self.ice[19+i][95] = " @ "

        #Add the boards
        for i in range(101):
            self.ice[0][i] = " # "
            self.ice[43][i] = " # "
        for i in range(44):
            self.ice[i][0] = " # "
            self.ice[i][100] = " # "

        # Add the puck to the center of the ice
        self.ice[21][50] = " *  "

    def get_name(self):
        return self.name
    
    def get_capacity(self):
        return self.capacity
    
    def get_teams(self):
        return self.teams
    
    # Print out the ice
    def print_ice(self):
        for row in self.ice:
            for square in row:
                print(square, end="")
            print()

