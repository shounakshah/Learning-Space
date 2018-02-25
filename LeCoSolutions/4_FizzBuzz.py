# Write a program that outputs the string representation of numbers from 1 to n.
#
# But for multiples of three it should output “Fizz” instead of the number
# And for the multiples of five output “Buzz”.
# For numbers which are multiples of both three and five output “FizzBuzz”.
#
# Example:
#
# n = 15,
#
# Return:
# [
#     "1",
#     "2",
#     "Fizz",
#     "4",
#     "Buzz",
#     "Fizz",
#     "7",
#     "8",
#     "Fizz",
#     "Buzz",
#     "11",
#     "Fizz",
#     "13",
#     "14",
#     "FizzBuzz"
# ]

from random import *

n = randint(1, 50)
print(f"n is: {n}")

if n is 1:
    print([str(1)])
else:
    my_list = []
    for number in range(1, n + 1):
        # If divisible by both 3 and 5, append FizzBuzz
        if number % 3 is 0 and number % 5 is 0:
            my_list.append("FizzBuzz")
        # Else, if divisible by 3, append Fizz
        elif number % 3 is 0:
            my_list.append("Fizz")
        # Else, if divisible by 5, append Buzz
        elif number % 5 is 0:
            my_list.append("Buzz")
        # Else, append the number itself
        else:
            my_list.append(str(number))
    print(f"String representation for '{n}' is: {my_list}")