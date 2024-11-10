"""This file is for challenge question 5."""

__author__ = "730813763"

def manual_append(list: list[int], value: int) -> None:
    """ Appends a value to the end of the provided list. """
    
    # Slicing the list and assigning the new value
    list[len(list):] = [value]


def double(list: list[int]) -> None:
    """ Doubles each value in the argument list. """

    i: int = 0  # For looping through the array
    while i < len(list):
        # Multiplies each element by 2
        list[i] *= 2
        i += 1 


list_1: list[int] = [1, 2, 3]
list_2: list[int] = list_1

double(list_2)

print(list_1)
print(list_2)