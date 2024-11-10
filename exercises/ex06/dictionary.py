""" This file is for exercise 6"""
__author__ = "730813763"

def invert(dictionary: dict[str, str]) -> dict[str, str]:
    """Inverts keys and values in the input dictionary."""
    new_dict: dict[str, str] = {}
    for key in dictionary:
        value = dictionary[key] 

        duplicate = False
        for duplicate_value in new_dict:
            if duplicate_value == value:
                duplicate = True
        if duplicate == True: # Raise error if there are duplicate values
            raise KeyError("Duplicate value detected in input dictionary!")
        new_dict[value] = key
    return new_dict # Returns the new dict


def favorite_color(favorites: dict[str, str]) -> str:
    """Returns the most popular color from the input dictionary"""
    new_dict: dict[str, int] = {}
    for name in favorites:
        color = favorites[name]  
        # Check if color is already in new_dict
        duplicate = False
        for duplicate_colors in new_dict:
            if duplicate_colors == color:
                duplicate = True
        if duplicate == True:
            # Increase count if color already exists
            new_dict[color] += 1
        else:
            # Reset the count
            new_dict[color] = 1
    
    most_common = "" # Make an empty string for outputting most common color
    max_count = -5 # Since all counts are positive
    for color in new_dict: # Loops thourgh the count of each colors
        count = new_dict[color] 
        if count > max_count:
            max_count = count # Changes the max count and most_common color when there is a more common color than the existing value.
            most_common = color
    return most_common

def count(items: list[str]) -> dict[str, int]:
    """Returns a dictionary of counts of each item"""
    new_dict: dict[str, int] = {}
    for i in items:
        # Check if item already exists in new_dict
        duplicate = False
        for duplicate_item in new_dict:
            if duplicate_item == i:
                duplicate = True
        if duplicate == True:
            # Increase count 
            new_dict[i] += 1
        else:
            # Reset the count
            new_dict[i] = 1
    return new_dict

def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Categorizes words by their starting letter"""
    new_dict: dict[str, list[str]] = {}
    for word in words:
        first_letter = word[0].lower() # So that lower case and upper case letters are not categorized differently
        # Check if first_letter is already in new_dict
        duplicate = False
        for duplicate_letter in new_dict:
            if duplicate_letter == first_letter:
                duplicate = True
        if duplicate:
            # Append word to existing letter category
            new_dict[first_letter].append(word)
        else:
            # Make a new category for a different letter
            new_dict[first_letter] = [word]
    return new_dict


def update_attendance(attendance_log: dict[str, list[str]], day: str, student: str) -> None:
    """Updates attendance log by adding a student to the inputted day"""
    # Check if day already exists in attendance_log
    duplicate = False
    for duplicate_day in attendance_log:
        if duplicate_day == day:
            duplicate = True
    if duplicate == True:
        # Check if student is already listed for that day
        student_duplicate = False
        for duplicate_student in attendance_log[day]:
            if duplicate_student == student:
                student_duplicate = True
        # Append student if not already there that day
        if student_duplicate != True:
            attendance_log[day].append(student)
    else:
        # Initialize a new day with the student if it doesn't exist
        attendance_log[day] = [student]
    return None