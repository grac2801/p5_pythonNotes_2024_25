'''
Created on Feb 19, 2025

@author: ogracias
'''
import random

class Dice:

    def __init__(self, playerName):
        self.playerName = playerName
        self.total = 0
        self.die1 = 0
        self.die2 = 0
        
    def tossDice(self):
        self.die1 = random.randint(1, 6)
        self.die2 = random.randint(1, 6)
        self.total = self.die1 + self.die2
        return self.total
    
    def printDice(self):
        print(f"Die 1 has a value of: {self.die1}")
        print(f"Die 2 has a value of: {self.die2}")
        
    def compareScores(self, other): 
        if self.total == other.total:
            print(f"{self.playerName} is tied with {other.playerName} at {self.total} points") 
        elif self.total < other.total:
            print(f"{other.playerName} wins with {other.total} points") 
        else:
            print(f"{self.playerName} wins with {self.total} points")
        
        
        
        
        