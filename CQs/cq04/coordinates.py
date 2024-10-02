"""This file is used to create get_coordinates function"""

__author__ = "730813763"


def get_coordinates(xs: str, ys: str) -> None:
    """Returns the formatted pair of each character in two strings"""

    # Created to use as indexes of strings in loops
    i: int = 0
    c: int = 0

    # i must be smaller than the length of the string to not get an index out of bounds error.
    while i < len(xs):
        while c < len(ys):
            print(f"({xs[i]},{ys[c]})")
            c+=1
        c = 0
        i+= 1

# function called with arguments "hi" and "bye"
get_coordinates("hi", "bye")