# nternational Morse Code defines a standard encoding where each letter is mapped to a series of dots and dashes,
# as follows: "a" maps to ".-", "b" maps to "-...", "c" maps to "-.-.", and so on.
#
# For convenience, the full table for the 26 letters of the English alphabet is given below:
#
# [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...",
# "-","..-","...-",".--","-..-","-.--","--.."]
# Now, given a list of words, each word can be written as a concatenation of the Morse code of each letter.
# For example, "cba" can be written as "-.-..--...", (which is the concatenation "-.-." + "-..." + ".-").
# We'll call such a concatenation, the transformation of a word.
#
# Return the number of different transformations among all words we have.
#
# Example:
# Input: words = ["gin", "zen", "gig", "msg"]
# Output: 2
# Explanation:
# The transformation of each word is:
# "gin" -> "--...-."
# "zen" -> "--...-."
# "gig" -> "--...--."
# "msg" -> "--...--."
#
# There are 2 different transformations, "--...-." and "--...--.".
# Note:
#
# The length of words will be at most 100.
# Each words[i] will have length in range [1, 12].
# words[i] will only consist of lowercase letters.
#
# Runtime: 36 ms
# Beats: 98.80%

words = ["gin", "zen", "gig", "msg"]

key = 'a';
morse_values = (".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-.", "---",
                ".--.", "--.-", ".-.", "...", "-", "..-", "...-", ".--", "-..-", "-.--", "--..")

#  Create a dictionary of alphabets and corresponding morse codes
morse_dictionary = {}
for code in morse_values:
    morse_dictionary[key] = code
    key = chr(ord(key) + 1)

# Print the Morse Code dictionary
print(f"Morse Code for every alphabet is: {morse_dictionary}")

# Convert given words to morse code and insert in a set to find the count of unique
set_of_unique_morse_code = set()

for word in words:
    code_for_this_word = ""
    for letter in word:
        code_for_this_word += morse_dictionary[letter]
    set_of_unique_morse_code.add(code_for_this_word)

print(f"All the uniques codes from the list of words are: {set_of_unique_morse_code}")
print(f"Total number of uniques morse codes are: {len(set_of_unique_morse_code)}")