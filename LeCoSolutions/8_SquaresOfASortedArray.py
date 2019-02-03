# Given an array of integers A sorted in non-decreasing order, return an array of the squares of each number,
# also in sorted non-decreasing order.
#
#
# Example 1:
#
# Input: [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Example 2:
#
# Input: [-7,-3,2,3,11]
# Output: [4,9,9,49,121]
#
#
# Note:
#
# 1 <= A.length <= 10000
# -10000 <= A[i] <= 10000
# A is sorted in non-decreasing order.
#
# Runtime: 144ms
# Beats: 90%

# A = [-4, -1, 0, 4, 10]
A = [-7, -3, 2, 3, 11]

# Create an empty list to store squared elements
my_squared_array = []
for number in A:
    my_squared_array.append(number * number)

# Sort the list of squared elements
my_squared_array.sort()

print(f"Sorted array of squares of {A} is: {my_squared_array}")
