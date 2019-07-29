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
    """
    When given an input string and list of available characters,
    will determine whether the string can be produced from the available characters,
    without re-using any of the characters,
    and allowing for uppercase & lowercase to be interchanged,
    along with some bonus character substitutions like '3' --> 'E' and '1' --> 'l'

    :param ransom_note: Input String, e.g., Hello
    :param magazine: List of available characters, e.g., ["h", "o", "l", "e", "l", ".", "?", "a", "b", "c"]
    :return: Boolean, True if string can be produced, False otherwise
    """
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
    flag = substitute_similar_characters(count_of_available_letters)
    if flag is True:
        print("Dictionary for Available Letters after substitution --> " + str(count_of_available_letters))
    else:
        print("!!!!!! Character substitution for Available Letters failed !!!!!!")

    # Create dictionary for ransom note letters
    count_of_ransom_note_letters = collections.Counter(ransom_note.lower())
    print("Dictionary for Ransom Note Letters --> " + str(count_of_ransom_note_letters))

    # Account for character substitution in available letters
    # Skip this substitution in available letters failed
    if flag is True:
        status = substitute_similar_characters(count_of_ransom_note_letters)
        if status is True:
            print("Dictionary for Ransom Note Letters after substitution --> " + str(count_of_ransom_note_letters))
        else:
            print("!!!!!! Character substitution for Ransom Note failed !!!!!!")
    else:
        print("!!!!!! Character substitution for Ransom Note skipped !!!!!!")

    for letter in count_of_ransom_note_letters:
        if letter not in count_of_available_letters:
            return False
        elif count_of_ransom_note_letters[letter] > count_of_available_letters[letter]:
            return False

    return True


def substitute_similar_characters(character_dictionary):
    """
    Takes input as a dictionary and adds the count of characters 3, 1, 0, @, $ to count of similar characters -
    e, l, o, a and s, since both of these could be used interchangeably.
    :param character_dictionary: dictionary of character counts
    :return: True, if function executed successfully, False otherwise
    """
    if not character_dictionary:
        return False

    if type(character_dictionary) != collections.Counter:
        return False

    words_to_be_substituted = {  # This dictionary contains characters valid for substitution to use in ransom note
        '3': 'e',  # e will account for e and E
        '1': 'l',  # l will account for l and L
        '0': 'o',  # o will account for o and O
        '@': 'a',  # a will account for a and A
        '$': 's'   # s will account for s and S
    }
    for letter in words_to_be_substituted:
        if letter in character_dictionary:
            # Add the count of a character like '3' to character like 'e'
            character_dictionary[words_to_be_substituted[letter]] = \
                character_dictionary[words_to_be_substituted[letter]] + character_dictionary[letter]
            # Delete the count of character like '3'
            del character_dictionary[letter]

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
      str(can_construct("ELOAS", ["3", "1", "0", "@", "$", "3", "1", "0", "@", "$"])) + '\n')
print(f'Can the ransom note be constructed --> '
      f'{can_construct("310@$", ["E", "L", "O", "A", "S"])} \n')
print(f'Can the ransom note be constructed --> '
      f'{can_construct("310@$", ["3", "1", "0", "@", "$"])} \n')

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
print('Can the ransom note be constructed --> ' + str(can_construct([1], ['H'])) + '\n')

print('------ Type of available words is not list ------')
print('Can the ransom note be constructed --> ' + str(can_construct("hello", 'H')) + '\n')

