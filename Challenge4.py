"""
Write a function, that reads an array of strings which will represent a list of comma-separated numbers sorted in
ascending order, the second element will represent a second list of comma-separated numbers(also sorted). Your goal is
to return a string of numbers that occur in both elements of the input array in sorted order. If there is no
intersection, return the string 'false'.

For example: if the input array is ['1, 3, 4, 7, 13', '1, 2, 4, 13, 15'] the output string should be '1, 4, 13' because
those number appear in both strings. The array given will not be empty, and each string inside the array will be of
numbers sorted in ascending order and may contain negative numbers.
"""

# SOLUTION-1 : BRUTE FORCE

import array as arr


def find_intersection(input_arr1, input_arr2):
    input_array1 = arr.array('u', input_arr1)
    input_array2 = arr.array('u', input_arr2)

    print(input_array1)
    print(input_array2)

    input_array1_list = list



find_intersection('1, 3, 4, 7, 13', '1, 2, 4, 13, 15')
