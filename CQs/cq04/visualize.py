"""This file is used to unite the functions written in other two files and visualize the results"""

__author__ = "730813763"

# Importing the functions in other files
from concatenation import concat
from coordinates import get_coordinates

# Creating two string variables to use as arguments for two functions imported
x = "123"
y = "abc"

print(concat(x,y))
get_coordinates(x,y)