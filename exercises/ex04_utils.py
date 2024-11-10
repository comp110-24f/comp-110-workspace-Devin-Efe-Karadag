""" This file is for exercise 4: list utility functions"""
__author__ = "730813763"


def all(list: list[int], val: int) -> bool:
    """Returns True if the first argument list only consists of integer val"""
    if len(list) == 0: # Checks for the edge case
        return False
    for num in list: # Looping through each element to check for equality
        if num != val: 
            return False # Returns False if values are not equal 
    return True # If the first return statement does not run, that means all values are equal.

def max(list: list[int]) -> int:
    """Returns the max integer value in a list consisting integers"""
    if len(list) == 0:
        raise ValueError("max() arg is an empty List")
    max = list[0] # assigning the first value to max variable to check if any other value is greater than the first one
    for val in list:
        if val > max: # checking each element 
            max = val # if any value is greater than the one in index 0, that becomes the max value.

    return max

def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Returns true if two list arguments are equal. Returns false otherwise."""
    return list_1 == list_2

def extend(list_1: list[int], list_2: list[int]) -> None:
    """Modifies the first list argument by concatinating it with the second list argument """
    list_1 += list_2

