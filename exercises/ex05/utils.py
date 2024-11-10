__author__ = "730813763"

def only_evens(list: list[int]) -> list[int]:
    """returns a list consisting only of even integers of the argument list. """
    new_list = [] # Creates an empty list
    
    for num in list:
        if num % 2 == 0:
            new_list.append(num) # All values in the argument list that are even are added to the new list.
    return new_list 


def sub(list: list[int], start_intex: int, end_index: int) -> list[int]:
    """Returns a slice of the argument list """
    new_list = list[start_intex:end_index] # takes a slice of the argument list based on the arguments start_index and end_index
    return new_list

def add_at_index(list: list[int], value: int, index: int) -> None:
    """Adds the argument value to the specified index on the list"""
    if index > len(list) or index < 0: # Raises error if index is out of bounds
        raise IndexError("Index is out of bounds for the input list")
    
    new_list = []
    for i in range(len(list)): # Loops through all elements in the list
        if i == index: 
            new_list.append(value) # Adds the new value to the intended index 
        new_list.append(list[i]) # Continues adding value that was previously on the argument index
    
    if index == len(list):
        new_list.append(value) # Handles the case where the value is to be added at the end of the list
    
    for i in range(len(new_list)):
        if i < len(list):
            list[i] = new_list[i] # Modifies the argument list with the new list
        else:
            list.append(new_list[i]) # Since the length of the new list increased by one, it appends the last element








