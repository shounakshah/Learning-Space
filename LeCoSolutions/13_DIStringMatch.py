# Given a string S that only contains "I" (increase) or "D" (decrease), let N = S.length.
#
# Return any permutation A of [0, 1, ..., N] such that for all i = 0, ..., N-1:
#
# If S[i] == "I", then A[i] < A[i+1]
# If S[i] == "D", then A[i] > A[i+1]
#
#
# Example 1:
#
# Input: "IDID"
# Output: [0,4,1,3,2]
# Example 2:
#
# Input: "III"
# Output: [0,1,2,3]
# Example 3:
#
# Input: "DDI"
# Output: [3,2,0,1]
#
#
# Note:
#
# 1 <= S.length <= 10000
# S only contains characters "I" or "D".
#
#
# Runtime: 76 ms
# Faster than: 100.00%

# S = "IDID"
# S = "III"
S = "DDI"

# Idea is to have 2 different values bigger and smaller
# Then when we hit an I select the current smaller value and increment it by 1
# Then when we hit D, select the current larger value and decrement it by 1
smaller_value = 0
larger_value = len(S)

A = []
for value in S:
    if value is "I":
        A.append(smaller_value)
        smaller_value += 1
    else:
        A.append(larger_value)
        larger_value -= 1

A.append(smaller_value)

print(f"Permutation for {S} is: {A}")
print(f"Smaller value = {smaller_value}")
print(f"Larger value = {larger_value}")