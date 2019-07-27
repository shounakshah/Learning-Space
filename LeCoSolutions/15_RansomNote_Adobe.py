# Examples
# input: "Hello"
# list of available characters: [ "h", "o", "l", "e", "l", ".", "?", "a", "b", "c" ]
# return: true
#
# input: "We hav yr cat, give us ur $"
# list: [ "a", "a" , "b", "&" ]
# return: false
# Bonus
# Support character substitution to allow interchangeable characters to be used
# e.g. an optional list of interchangeable characters
#
# input: "hello"
# list: [ "h", "o", "l", "3", "1",]
# interchange: { 'e' -> '3', 'l' -> '1' }
# return: true

import collections


def can_construct(ransom_note, magazine):
    # Type check for input variables,
    # ransom_note should be a string, if not return false
    # magazine should be a list, if not return false
    if type(ransom_note) != str or type(magazine) != list:
        return False

    # Check for empty string or empty list, return false if any one empty
    if not ransom_note or not magazine:
        return False
    print("Ransom Note words are: " + ransom_note)
    print("Available letters are: " + str(magazine))

    # If the ransom note is bigger than available words, return False
    if len(ransom_note) > len(magazine):
        return False

    # Create dictionary for available letters
    count_of_available_letters = collections.Counter((''.join(magazine)).lower())
    print("Dictionary for Available Letters before substitution --> " + str(count_of_available_letters))

    # Account for character substitution in available letters
    words_to_be_substituted = {  # This dictionary contains characters valid for substitution to use in ransom note
        '3': 'e',  # e will account for e and E
        '1': 'l',  # l will account for l and L
        '0': 'o',  # o will account for o and O
        '@': 'a',  # a will account for a and A
        '$': 's'   # s will account for s and S
    }
    for letter in words_to_be_substituted:
        if letter in count_of_available_letters:
            # Add the count of a character like '3' to character like 'e'
            count_of_available_letters[words_to_be_substituted[letter]] = \
                count_of_available_letters[words_to_be_substituted[letter]] + count_of_available_letters[letter]
            # Delete the count of character like '3'
            del count_of_available_letters[letter]
    print("Dictionary for Available Letters after substitution --> " + str(count_of_available_letters))

    # Create dictionary for ransom note letters
    count_of_ransom_note_letters = collections.Counter(ransom_note.lower())
    print("Dictionary for Ransom Note Letters --> " + str(count_of_ransom_note_letters))

    for letter in count_of_ransom_note_letters:
        if letter not in count_of_available_letters:
            return False
        elif count_of_ransom_note_letters[letter] > count_of_available_letters[letter]:
            return False

    return True


# Example Inputs
print('------ Example Inputs ------')
print('Can the ransom note be constructed --> ' +
      str(can_construct("Hello", ["h", "o", "l", "e", "l", ".", "?", "a", "b", "c"])) + '\n')
print('Can the ransom note be constructed --> ' +
      str(can_construct("We hav yr cat, give us ur $", ["a", "a" , "b", "&"])) + '\n')

# Bonus Inputs
print('------ Bonus Inputs ------')
print('Can the ransom note be constructed --> ' + str(can_construct("hello", ["h", "o", "l", "3", "1"])) + '\n')
print('Can the ransom note be constructed --> ' +
      str(can_construct("ELOAS", ["3", "1", "0", "@", "S", "3", "1", "0", "@", "S"])) + '\n')

# Failure / Edge Case Inputs
print('------ Failure / Edge Case Inputs ------')

# Empty ransom note
print('------ Empty Ransom Note ------')
print('Can the ransom note be constructed --> ' + str(can_construct("", ["h", "o", "l", "3", "1"])) + '\n')

# Empty list
print('------ Empty available word list ------')
print('Can the ransom note be constructed --> ' + str(can_construct("hello", [])) + '\n')

# Ransom Note bigger than available letters
print('------ Ransom note has more letters than available letters ------')
print('Can the ransom note be constructed --> ' + str(can_construct("hello", ['H'])) + '\n')

# Input Type Check for can_construct function
print('------ Type of Ransom Note is not string ------')
print('Can the ransom note be constructed --> ' + str(can_construct(1, ['H'])) + '\n')

print('------ Type of available words is not list ------')
print('Can the ransom note be constructed --> ' + str(can_construct("hello", 'H')) + '\n')

