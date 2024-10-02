""" This file is for exercise 3: coding a wordle game"""
__author__ = "730813763"



def input_guess(secret_word_len: int) -> str:
    """Returns the user's string input if the string has the same length as the secret word. Loops through the same process otherwise. """
    
    ans = input(f"Enter a {secret_word_len} character word: ") # input is assigned 
    while len(ans) != secret_word_len: # if they are not in the same length the program asks for input once again until the condition is satisfied.
        ans = input(f"That wasn't {secret_word_len} chars! Try again: ")
    print(ans)
    return ans


def contains_char(secret_word: str, char_guess: str) -> bool:
    """Returns True if char exists in secret_word. Returns False otherwise."""
    assert len(char_guess) == 1 # Making sure second argument is a char.
    i: int = 0 
    while i < len(secret_word): # To loop through each char in string while not getting an index error.
        if secret_word[i] == char_guess:
            return True # Returns True if it's found.
        i+=1
    return False # Returns false if char does not exist in the secret string.

def emojified(secret_word: str, user_guess: str) -> str:
    """Prints the "wordle output" to the screen based on the comparison between user's guess and secret_word."""
    assert len(secret_word) == len(user_guess) # Making sure both have the same length
    # Color constants for the print statement 
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    output: str = "" # Output is added "after" the comparison
    i: int = 0
    while i < len(secret_word):
        if user_guess[i] == secret_word[i]: # Prints green when the user_guess contains the same letter in the correct position
            output += GREEN_BOX
        elif contains_char(secret_word, user_guess[i]): # Prints yellow if the letter exists but not in the correct position
            output += YELLOW_BOX
        else: # Prints white if the letter guessed does not exist in the secret_word
             output+= WHITE_BOX
                
        i+= 1
             
    return output


def main(secret_word: str) -> None: 

    i: int = 0
    while i < 6: # User has 6 turns to find the correct answer
        print(f"=== Turn {i+1}/6 ===")
        user_guess=input_guess(len(secret_word))
        output = emojified(secret_word=secret_word, user_guess=user_guess) # Prints the wordle output 
        print(output)
        if secret_word == user_guess: # ends the program if the user guesses correctly
            print(f"You won in {i+1}/6 turns!")
            return
        i+=1

    print("X/6 - Sorry, try again tomorrow!") # If the answer is not found. The program prints this statement, then quits.

if __name__ == "__main__":
    main(secret_word="codes") # the argument here is the secret_word