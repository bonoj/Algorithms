# Binary Search

"""You're going to write a binary search function.
You should use an iterative approach - meaning
using loops.
Your function should take two inputs:
a Python list to search through, and the value
you're searching for.
Assume the list only has distinct elements,
meaning there are no repeated values, and
elements are in a strictly increasing order.
Return the index of value, or -1 if the value
doesn't exist in the list."""

def binary_search(input_array, value):
    low = 0
    high = len(input_array) - 1
    while (low <= high):
        mid = int((low + high) / 2)
        if (input_array[mid] == value):
            return mid
        elif (input_array[mid] < value):
            low = mid + 1
        else:
            high = mid - 1
    return -1



# test_list = [1, 3, 9, 11, 15, 19, 29]
# test_val1 = 25
# test_val2 = 15
# print(binary_search(test_list, test_val1))
# print(binary_search(test_list, test_val2))

# Recursion
# def recur(input):
#     if input <= 0:
#         print("At base case.")
#         return "Done."
#     else:
#         print("Recurring with input: " + str(input-1))
#         output = recur(input - 1)
#         return output
#
# print(recur(5))

# # """Implement a function recursivly to get the desired
# # Fibonacci sequence value.
# # Your code should have the same input/output as the
# # iterative code in the instructions."""
#
# def get_fib(position):
#     if position <= 0:
#         return 0
#     if position == 1:
#         return 1
#     else:
#         value = get_fib(position - 1) + get_fib(position - 2)
#         return value
#
# # Test cases
# # for i in range(15):
# #     print(i, get_fib(i))
#
# def get_fib_iterative(position):
#     if position <= 0:
#         return 0
#     if position == 1:
#         return 1
#     first = 0
#     second = 1
#     next = first + second
#     i = 3
#     while i <= position:
#         i += 1
#         first = second
#         second = next
#         next = first + second
#     return next
#
# # Test cases
# for i in range(15):
#     print(i, get_fib_iterative(i))



# def recursive_binary_search(input_array, value):
#     print(input_array)
#     mid = int(len(input_array) / 2)
#     if len(input_array) == 1 and input_array[0] != value:
#         return -1
#     elif len(input_array) == 1 and input_array[0] == value:
#         return value
#
#     if len(input_array) % 2 == 0:
#         if value == input_array[int((len(input_array)) / 2) - 1]:
#             return int((len(input_array) / 2)) - 1
#         elif value > input_array[int((len(input_array)) / 2) - 1]:
#             p = recursive_binary_search(input_array[(int((len(input_array)) / 2)):], value)
#             return p
#         else:
#             p = recursive_binary_search(input_array[:(int((len(input_array)) / 2))], value)
#             return p
#
#     else:
#         if value == input_array[int(len(input_array) / 2)]:
#             return int(len(input_array) / 2)
#         elif value > input_array[int(len(input_array) / 2)]:
#             # print(input_array[int(len(input_array) / 2):])
#             p = recursive_binary_search(input_array[int(len(input_array) / 2):], value)
#             return p
#         else:
#             # print(input_array[:int(len(input_array) / 2)])
#             p = recursive_binary_search(input_array[:int(len(input_array) / 2)], value)
#             return p
#
# test_list = [1, 3, 9, 11, 15, 19, 29, 30]
# test_val1 = 25
# test_val2 = 15
# print(recursive_binary_search(test_list, test_val1))
# print(recursive_binary_search(test_list, test_val2))
