# Given a string, you need to reverse the order of characters in each word within a sentence
# while still preserving whitespace and initial word order.
#
# Example 1:
# Input: "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
#
# Note: In the string, each word is separated by single space and there will not be any extra space in the string.

s = "Let's take LeetCode contest"

# Reverse the original string
# Split the reversed string at every space
reversed_split_string = s[::-1].split()

# Concatenate the string
reversed_string = ""
for word in reversed_split_string:
    if reversed_string is "":
        reversed_string = word
    else:
        # "word" will come before "reversed_string" as I had originally split the reversed string
        reversed_string = word + " " + reversed_string

# Print the reversed string
print(f"Reverse of {s} is: {reversed_string}")