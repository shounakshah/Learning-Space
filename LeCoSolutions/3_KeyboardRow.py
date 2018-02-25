# Given a List of words,
# return the words that can be typed using letters of alphabet on only one row of American keyboard (QWERTY)
#
# Example 1:
# Input: ["Hello", "Alaska", "Dad", "Peace"]
# Output: ["Alaska", "Dad"]
#
# Note:
# You may use one character in the keyboard more than once.
# You may assume the input string will only contain letters of alphabet.

# Runtime: 36 ms
# Beats: 100%

words = ["Hello", "Alaska", "Dad", "Peace"]

row1 = set(['q', 'w', 'e', 'r', 't', 'y', 'u', 'i', 'o', 'p'])
row2 = set(['a', 's', 'd', 'f', 'g', 'h', 'j', 'k', 'l'])
row3 = set(['z', 'x', 'c', 'v', 'b', 'n', 'm'])

my_list = []
# For every word in words
for word in words:
    # Check if the first letter in in row1
    if word[0].lower() in row1:
        # If any of the other letters for that word are not in the same row, break
        for letter in word[1:]:
            if letter.lower() not in row1:
                break
        # Else add word to a list
        else:
            my_list.append(word)
    # Else, Check if the first letter in row2
    elif word[0].lower() in row2:
        # If any of the other letters for that word are not in the same row, break
        for letter in word[1:]:
            if letter.lower() not in row2:
                break
        # Else add word to a list
        else:
            my_list.append(word)
    # Else, Check if the first letter in row3
    elif word[0].lower() in row3:
        # If any of the other letters for that word are not in the same row, break
        for letter in word[1:]:
            if letter.lower() not in row3:
                break
        # Else add word to a list
        else:
            my_list.append(word)

print(f"Words from {words} that can be typed only using one row on American Keyboard are: {my_list}")
