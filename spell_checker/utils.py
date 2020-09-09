import re
from typing import List, Tuple


def build_regex(string: str) -> re.Pattern:
    """
    Build a regex pattern to fit desired specifications for allowable word matching.
    
    Currently, the specifications for allowed matches (ignoring capitalization) are:
    1) Superfluous repeated letters
    2) Missing vowels
    """
    # Regex fragment representing zero or more vowels
    any_vowels = '[aeiou]*'

    # Initialize regex string, allowing for optional vowels at the start
    regex = any_vowels

    # Build the regex string, specifying max number of allowed repeats of each character and any vowels in between
    for character, repeats in get_character_repeats(string):
        regex += character + '{1,' + str(repeats) + '}' + any_vowels

    # Return the compiled regex pattern
    return re.compile(regex)


def get_character_repeats(string: str) -> List[Tuple[str, int]]:
    """
    Get the sequence of characters in a string with the number of times each is consecutively repeated.
    
    e.g. 'aaabbcaa' -> [('a', 3), ('b', 2), ('c', 1), ('a', 2)]
    """
    # Container to hold the counts of consecutively repeated characters in the string
    character_repeats = []

    # Calculate length of the string once (used a few times)
    string_length = len(string)

    # Handle the edge case of an empty string
    if string_length == 0:
        return character_repeats

    # Initialize variables for iteration, seeding with the first character of the string
    character = string[0]
    repeats = 1

    # Iterate over the string, starting at the second character given that first has no previous character 
    # to which to compare (and was instead used for initialization for the below algorithm)
    for i in range(1, string_length):

        # If the character is the same as the previous, incremement the current repeats count
        if string[i] == string[i-1]:
            repeats += 1
        
        # Otherwise, record the final number of repeats for the current character and initialize a new streak
        else:
            character_repeats.append((character, repeats))
            character = string[i]
            repeats = 1
    
        # Account for the current streak if we've reached the last character
        if i == string_length - 1:
            character_repeats.append((character, repeats))

    return character_repeats


def is_correct_format(string: str) -> bool:
    """
    Check whether a string is of an allowable format. 
    
    Currently, this is just checking that capitalization falls under one of three cases:
    1) All lowercase
    2) All upppercase
    3) Title case (fist letter capitalized)
    """
    return string.islower() or string.isupper() or string.istitle()
