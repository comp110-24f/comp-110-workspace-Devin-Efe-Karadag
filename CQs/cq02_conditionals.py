"""This file is for cq02"""

__author__ = "730813763"
secret: int = 7

def guess_a_number() -> None: 
    """Asks for input and compares to the secret number"""
    num = int(input("Guess a number: "))
    print(f"Your guess was {num}")
    if num < secret:
      print(f"Your guess was too low! The secret number is {secret}")
    elif num > secret:
       print(f"Your guess was too high! The secret number is {secret}")
    else:
       print("You got it!")

def main() -> None:
   guess_a_number()

if __name__ == "__main__":
   main()