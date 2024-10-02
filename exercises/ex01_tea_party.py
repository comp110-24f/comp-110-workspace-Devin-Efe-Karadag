"""The program aims to output the amount of tea bags, treats and costs needed to attent to a tea party based on how many people are in the event which is specified by the user's input."""

__author__: str = "730813763"


def main_planner(guests: int) -> None:
    """outputs the user input with a sentence"""
    
    # Prints the number of guests
    print(f"A cozy tea party for {guests} people")
    # Prints the number of tea bags needed
    print(f"Tea Bags: {tea_bags(guests)}")
    # Prints the amount of treats needed
    print(f"Treats: {treats(guests)}")
    #Prints the cost of treats and tea bags
    print(f"Cost: ${cost(tea_bags(guests), treats(guests))}") # Prints all values in a sentence


def tea_bags(people: int) -> int:
    """Calculates the amount of teabags needed"""
    return people * 2 # returns 2 times the number of people


def treats(people: int) -> int:
    """ "Calculates the amount of treats needed"""
    return int(tea_bags(people=people) * 1.5) # Calls the tea_bags() function and returns 1.5 times of the tea_bags return value


def cost(tea_count: int, treat_count: int) -> float:
    """Calculates the cost of treats and tea_bags"""
    return treat_count * 0.75 + tea_count * 0.5 # Returns the overall cost by using the formula given in the question


# Calls the main_planner() function which serves to combine all other function calls and output them to the user
if __name__ == "__main__":
    """Main function call"""
    main_planner(guests=int(input("How many guests are attending to your tea party.")))
