"""File to define Fish class."""

__author__ = "730813763"


class Fish:
    age: int
    
    def __init__(self):
        self.age = 0
    
    def one_day(self):
        self.age += 1