"""This file is used to create the concat function"""

__author__ = "730813763"

def concat(str1: str, str2: str) -> str:
    """Returns the concatenation of two strings."""
    return str1 + str2

# Creating two strings to use the concat function
word1 = "happy"
word2 = "tuesday"


# Due to this condition, print statement won't run from importing the function
if __name__ == "__main__":
    print(concat(word1, word2))