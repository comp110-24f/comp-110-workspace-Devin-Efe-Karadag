"""While Loops Challenge Question (CQ03)"""

__author__ = "730813763"

# Takes strings phrase and search_char as argument 
def num_instances(phrase: str, search_char: str) -> int:
    """ Return an integer that represents how many letters there is in a given phrase"""
    # Used to count the number of search_char in the phrase
    count = 0
    # Used to loop through each index in the phrase
    index = 0
    # Loops through each index until the index equals length of the phrase
    while (index != len(phrase)):
        # Checks if the search_char equals the letter in phrase[index]
        if(phrase[index] == search_char):
            # If they are equal count is increased
            count += 1
        # Index increased by 1 to compare other indexes with the search_char
        index += 1
    # Number of search_char in phrase is returned 
    return count 

