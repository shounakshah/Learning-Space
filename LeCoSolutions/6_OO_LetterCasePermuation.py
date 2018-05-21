# Given a string S, we can transform every letter individually to be lowercase or uppercase to create another string.
# Return a list of all possible strings we could create.
#
# Examples:
# Input: S = "a1b2"
# Output: ["a1b2", "a1B2", "A1b2", "A1B2"]
#
# Input: S = "3z4"
# Output: ["3z4", "3Z4"]
#
# Input: S = "12345"
# Output: ["12345"]
# Note:
#
# S will be a string with length at most 12.
# S will consist only of letters or digits.

S = "a1b2"

# Need a list to add digits
# Use recursive strategy to pass a list
# Append lowercase and uppercase letter to every string in the list


def string_combinations(S, index, my_list = []):
    if index is len(S):
        return my_list
    new_list = []
    if S[index].isdigit():
        if len(my_list) is 0:
            new_list.append(S[index])
        else:
            for every_string in my_list:
                new_list.append(every_string + S[index])
    else:
        if len(my_list) is 0:
            new_list.append(S[index].lower())
            new_list.append(S[index].upper())
        else:
            for every_string in my_list:
                new_list.append(every_string + S[index].lower())
                new_list.append(every_string + S[index].upper())

    return string_combinations(S, index + 1, new_list)


print(f"All Combinations of {S} are: {string_combinations(S, 0)}")
