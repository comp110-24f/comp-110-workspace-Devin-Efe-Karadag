"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730813763"


def input_word() -> str:
    """Returns the string input if its length is 5. Exits the program otherwise."""

    # Input is assigned to the "word" variable
    word = input("Enter a 5-character word: ")
    
    # Checks if the length of the word is not 5 
    if len(word)!= 5:
     # Prints error for not following directions
     print("Error: Word must contain 5 characters.")
     # Quits the program
     exit()
    # Returns the input string if the user enters a word with length 5
    return word


def input_letter() -> str:
   """Returns the string input if its length is 1. Exits the program otherwise."""
   
   # Input is assigned to the "letter" variable
   letter = input("Enter a single character: ")
   # Checks if the length of the "letter" is not 1
   if len(letter)!= 1:  
    # Prints error for not following the direction
    print("Error: Character must be a single character.")
    # Quits the program
    exit()
   # Returns the input string if the user enters an input with length 1 
   return letter


def contains_char(word: str, letter: str) -> None:
   """Prints the number of inputted letter there is in a chosen word."""
  
   # Prints what the program is doing
   print(f"Searching for {letter} in {word}")
   # Two variables are created with int(0) 

   # Used to check each letter in the word for the loop's condition 
   index = 0
   # Used to count how many times the condition is satisfied
   count = 0

   # Loops until index does not reach to the length of the word
   while index != len(word):
      # Checks if the letter word[index] is same as the letter inputted by the user
      if(word[index] == letter):
       # Informs the user that letters match
       print(f"{letter} found at index {index}")
       # Count increased by 1
       count +=1
      # Index increased by 1 to loop through all elements
      index+=1

   # Conditions to check which print statement to use depending on the amount of matches.
   if count == 0:
      print(f"No instances of {letter} found in {word}")
   elif count == 1:
      print(f"1 instance of {letter} found in {word}")
   else:
      print(f"{count} instances of {letter} found in {word}")

# Calls the contains_char functions which uses all the other functions' return values in its definiton
def main() -> None:
   """Main function to run the program."""
   contains_char(word=input_word(), letter=input_letter())

# Runs the main() function 
if __name__ == "__main__":
   main()
