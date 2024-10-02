
""" asdfasdfasdfasf"""
__author__ = "730813763"

WHITE_BOX: str = "\U00002B1C"
GREEN_BOX: str = "\U0001F7E9"
YELLOW_BOX: str = "\U0001F7E8"

def input_guess(secret_word_len: int) -> str:
    ans = input(f"Enter a {secret_word_len} character word: ")
    while len(ans) != secret_word_len:
        ans = input(f"That wasn't {secret_word_len} chars! Try again: ")
    print(ans)
    return ans


def contains_char(secret_word: str, char_guess: str) -> bool:
    assert len(char_guess) == 1
    i: int = 0
    while i < len(secret_word):
        if secret_word[i] == char_guess:
            return True
    return False

def emojified(secret_word: str, user_guess: str) -> str:
    output: str = ""
    assert len(secret_word) == len(user_guess)
    i: int = 0
    while i < len(secret_word):
        if user_guess[i] == secret_word[i]:
            output += GREEN_BOX 

        else: 
            c: int = 0
            flag = False
            while c < len(secret_word):
                if user_guess[i] == secret_word[c]:
                    flag = True
                c += 1         
                
            if flag:
             output+= YELLOW_BOX
            else:
             output+= WHITE_BOX
                
        
        i+= 1
             
    
    return output



def main(secret_word: str) -> None:

    i: int = 0
    while i < 6:
        print(f"=== Turn {i+1}/6 ===")
        result = emojified(secret_word=secret_word, user_guess=input_guess(len(secret_word)))
        print(result)
        if result == len(secret_word) * GREEN_BOX:
            print(f"You won in {i+1}/6 turns!")
            quit()
        i+=1

    print("X/6 - Sorry, try again tomorrow!")

if __name__ == "__main__":
    main(secret_word="codess")