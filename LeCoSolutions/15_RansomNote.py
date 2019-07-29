# Given an arbitrary ransom note string and another string containing letters from all the magazines,
# write a function that will return true if the ransom note can be constructed from the magazines ;
# otherwise, it will return false.
#
# Each letter in the magazine string can only be used once in your ransom note.
#
# Note:
# You may assume that both strings contain only lowercase letters.
#
# canConstruct("a", "b") -> false
# canConstruct("aa", "ab") -> false
# canConstruct("aa", "aab") -> true

def canConstruct(ransomNote, magazine):
    print("Ransom Note words are: " + ransomNote)
    print("Available letters are: " + magazine)

    # If the ransom note is bigger than available words, return False
    if len(ransomNote) > len(magazine):
        return False

    # Create dictionary for available letters
    dictAvailableLetters = {}
    for letter in set(magazine.lower()):
        dictAvailableLetters[letter] = magazine.lower().count(letter)
    print("Dictionary for Available Letters --> " + str(dictAvailableLetters))

    # Create dictionary for ransom note letters
    dictRansomNote = {}
    for letter in set(ransomNote.lower()):
        dictRansomNote[letter] = ransomNote.lower().count(letter)
    print("Dictionary for Ransom Note Letters --> " + str(dictRansomNote))

    for letter in dictRansomNote:
        if letter not in dictAvailableLetters:
            return False
        elif dictRansomNote[letter] > dictAvailableLetters[letter]:
            return False

    return True

print("canConstruct --> " + str(canConstruct("aab", "aB")) + "\n")

print("canConstruct --> " + str(canConstruct("a", "b")) + "\n")
print("canConstruct --> " + str(canConstruct("aa", "ab")) + "\n")
print("canConstruct --> " + str(canConstruct("aa", "aab")) + "\n")

print("canConstruct --> " + str(canConstruct("hell", "hello")) + "\n")
print("canConstruct --> " + str(canConstruct("abb", "abbcccddddeeeeeffffff")) + "\n")
print("canConstruct --> " + str(canConstruct("Z", "aBcDeFgHiJkL")) + "\n")
