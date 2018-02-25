# Given a string, you need to reverse the order of characters in each word within a sentence
# while still preserving whitespace and initial word order.
#
# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
#
# Note: In the string, each word is separated by single space and there will not be any extra space in the string.

s = "Let's take LeetCode contest"

# Split the string at spaces
split_string = s.split()

# Reverse every word in the list
# And concatenate all the reversed words
reversed_string = ""
for word in split_string:
    if reversed_string is "":
        reversed_string = word[::-1]
    else:
        reversed_string = reversed_string + " " + word[::-1]

# Print the reversed string
print(f"Reverse of {s} is: {reversed_string}")