"""
Given an integer array, output all the unique pairs that sum up to a specific value k.

Input: pair_sum([1, 2, 4, 6], 3)

Output: (1, 2)
"""
from array import *


def pair_sum(arr, k):
    match_list = []
    for index in range(len(arr)):
        x = arr[index]
        for next_index in range(1, len(arr)):
            # when there's no match, this check will modify last iteration to NOT run out of bounds
            y = arr[next_index]

            if x is not None and y is not None:
                if x + y == k:
                    match_list.append((x, y))

    for item in match_list:
        print(item)

    return 'Number of unique pairs: {}'.format(len(match_list))


print(pair_sum([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10))


def pair_sum2(arr, k):
    if len(arr) < 2:
        return 'less than 2 elements in the set'

    # Sets for tracking
    seen = set()
    output = set()

    for num in arr:
        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            output.add(((min(num, target)), max(num, target)))

    # return len(output)
    print('\n'.join(map(str, list(output))))


print(pair_sum2([1, 9, 2, 8, 3, 7, 4, 6, 5, 5, 13, 14, 11, 13, -1], 10))
