# You're now a baseball game point recorder.
#
# Given a list of strings, each string can be one of the 4 following types:
#
# 1.    Integer (one round's score): Directly represents the number of points you get in this round.
#
# 2.    "+" (one round's score): Represents that the points you get in this round
#       are the points_sum of the last two valid round's points.
#
# 3.    "D" (one round's score): Represents that the points you get in this round
#       are the doubled data of the last valid round's points.
#
# 4.    "C" (an operation, which isn't a round's score): Represents the last valid round's points you get
#       were invalid and should be removed.
#
# Each round's operation is permanent and could have an impact on the round before and the round after.
#
# You need to return the points_sum of the points you could get in all the rounds.
#
# Example 1:
#
# Input: ["5","2","C","D","+"]
#
# Output: 30
#
# Explanation:
# Round 1: You could get 5 points. The points_sum is: 5.
# Round 2: You could get 2 points. The points_sum is: 7.
# Operation 1: The round 2's data was invalid. The points_sum is: 5.
# Round 3: You could get 10 points (the round 2's data has been removed). The points_sum is: 15.
# Round 4: You could get 5 + 10 = 15 points. The points_sum is: 30.
#
#
# Example 2:
#
# Input: ["5","-2","4","C","D","9","+","+"]
#
# Output: 27
#
# Explanation:
# Round 1: You could get 5 points. The points_sum is: 5.
# Round 2: You could get -2 points. The points_sum is: 3.
# Round 3: You could get 4 points. The points_sum is: 7.
# Operation 1: The round 3's data is invalid. The points_sum is: 3.
# Round 4: You could get -4 points (the round 3's data has been removed). The points_sum is: -1.
# Round 5: You could get 9 points. The points_sum is: 8.
# Round 6: You could get -4 + 9 = 5 points. The points_sum is 13.
# Round 7: You could get 9 + 5 = 14 points. The points_sum is 27.
#
#
# Note:
# The size of the input list will be between 1 and 1000.
# Every integer represented in the list will be between -30000 and 30000.
#
# Runtime: 40ms
# Beats: 100%

ops = ["5", "-2", "4", "C", "D", "9", "+", "+"]

# Need a stack to store all points
points_stack = []
# Need an integer to store points_sum of points
points_sum = 0

# Look at current round's points
for points in ops:

    # If D, access last point in the stack -> double it -> add to points_sum -> push current points to stack
    if points is "D" and len(points_stack) is not 0:
        points_sum = points_sum + 2 * points_stack[-1]
        points_stack.append(2 * points_stack[-1])

    # If +, access last 2 points in the stack -> add both of them ->
    # add them to points_sum -> push the addition to stack
    elif points is "+" and len(points_stack) is not 0:
        if len(points_stack) is 1:
            points_sum = points_sum + points_stack[-1]
        else:
            points_sum = points_sum + points_stack[-1] + points_stack[-2]
            points_stack.append(points_stack[-1] + points_stack[-2])

    # If C, access last point in the stack -> subtract it from points_sum -> remove it from the stack
    elif points is "C" and len(points_stack) is not 0:
        points_sum = points_sum - points_stack.pop()

    # If integer, add to points_sum and then push in stack
    else:
        points_sum = points_sum + int(points)
        points_stack.append(int(points))

print(f"Total points earned for {ops} are: {points_sum}")
