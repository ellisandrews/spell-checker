# TODO: Delete this function?
def get_letter_sequence(string):
    """
    Determine the sequence of letters in a string (ignoring repeats).
    
    e.g. 'aAaaBBBbbbccAAa' -> ['a', 'b', 'c', 'a']
    """
    # Convert the string to lowercase
    string = string.lower()

    # List to hold the sequence of letters
    sequence = []

    # Iterate over the string to find the sequence of letters
    for i in range(len(string)):

        # The first letter doesn't have a previous letter to compare against
        if i == 0:
            sequence.append(string[i])
            continue

        # If the current letter is different from the previous letter, append it to the sequence
        if string[i] != string[i-1]:
            sequence.append(string[i])
    
    return sequence


def get_letter_repeats(string):
    """
    Determine the sequence of letters in a string with their consecutive repeat counts.
    
    e.g. 'aAaaBBBbbbccAAa' -> [('a', 4), ('b', 6), ('c', 2), ('a', 3)]
    """
    # Convert the string to lowercase
    string = string.lower()

    # Container to hold counts of consecutively repeated letters
    letter_repeats = []

    # Calculate this value only once
    string_length = len(string)

    # Initialize variables for iteration
    letter = string[0]
    repeats = 1

    # Iterate over the string, starting at the second letter given that first letter has no previous letter 
    # to compare to, and was used instead to initialize our iteration variable
    for i in range(1, string_length):

        # If the letter is the same as the previous, incremement the current repeats count
        if string[i] == string[i-1]:
            repeats += 1
        
        # Otherwise, record the number of repeats for the current letter and start a new streak
        else:
            letter_repeats.append((letter, repeats))
            letter = string[i]
            repeats = 1
    
        # Account for the current streak if we've reached the last letter
        if i == string_length - 1:
            letter_repeats.append((letter, repeats))

    return letter_repeats


def build_regex(letter_repeats):
    """
    Build a regex given a letter sequence with repeats.
    """
    # TODO: Consider decoupling vowel omission check from repeated characters check? i.e. Don't build a single regex?

    # Regex fragment representing zero or more vowels
    any_vowels = '[aeiou]*'

    # Initialize regex string, allowing for optional vowels at the start
    regex = any_vowels

    # Build the regex string, specifying max number of allowed repeats of each letter and any vowels in between
    for letter, repeats in letter_repeats:
        regex += letter + '{1,' + str(repeats) + '}' + any_vowels

    # Return the constructed regex string
    return regex
