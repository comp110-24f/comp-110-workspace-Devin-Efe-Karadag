"""File to define Bear class."""

__author__ = "730813763"

class Bear:
    age: int 
    hunger_score: int
    
    def __init__(self):
        self.age = 0
        self.hunger_score = 0
    
    def one_day(self):
        self.age += 1
        self.hunger_score -= 1

    def eat(self, num_fish: int):
        self.hunger_score += num_fish
