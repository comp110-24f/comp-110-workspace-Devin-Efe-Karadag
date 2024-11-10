"""This file is for cq07: Unit Test Challenge Question"""
__author__ = "730813763"



def find_and_remove_max(list: list[int]) -> int:
    """Removes the max integer from the argument list. Returns the max value."""
    if len(list) == 0: # handles the edge case
        return -1
    max = list[0]
    for i in range(len(list)):
        if list[i] > max:
            max = list[i] # Any value larger than the one in the first index gets assigned as max

    new_list = [] # Empty list for storing non-max values.
    for num in list:
        if num != max:
            new_list.append(num)
    
    list[:] = new_list # Argument is modified 
    return max
