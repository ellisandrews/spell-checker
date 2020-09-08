def get_character_repeats(string):
    """
    Get the sequence of characters in a string with the number of times each is consecutively repeated.
    
    e.g. 'aaabbcaa' -> [('a', 3), ('b', 2), ('c', 1), ('a', 2)]
    """
    # Container to hold the counts of consecutively repeated characters in the string
    character_repeats = []

    # Calculate length of the string once (used a couple times in iteration)
    string_length = len(string)

    # Initialize variables for iteration
    character = string[0]
    repeats = 1

    # Iterate over the string, starting at the second character given that first has no previous character 
    # with which to compare (and was instead used for initialization for the below algorithm)
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


def build_regex(character_repeats):
    """
    Build a regex given a letter sequence with repeats.
    """
    # TODO: Consider decoupling vowel omission check from repeated characters check? i.e. Don't build a single regex?

    # Regex fragment representing zero or more vowels
    any_vowels = '[aeiou]*'

    # Initialize regex string, allowing for optional vowels at the start
    regex = any_vowels

    # Build the regex string, specifying max number of allowed repeats of each character and any vowels in between
    for character, repeats in character_repeats:
        regex += character + '{1,' + str(repeats) + '}' + any_vowels

    # Return the constructed regex string
    return regex


def is_correct_format(string):
    """Check whether a string is of an allowable format. Currently just checking for correct capitalization."""
    return string.islower() or string.isupper() or string.istitle()
