# 767. Reorganize String
# Given a string S, check if the letters can be rearranged so that two characters that are adjacent to each other are not the same.
# https://leetcode.com/problems/reorganize-string/description/
import heapq
from collections import Counter
from itertools import count


def reorganize(input_string):
    s_dict = Counter(input_string)
    res = helper(s_dict)
    for i in range(len(res) - 1):
        if res[i] == res[i + 1]:
            return ""
    return res


def helper(s_dict):
    res = ""
    for key, value in s_dict.items():
        if value > 0:
            res += key
            s_dict[key] -= 1

    for key in list(s_dict.keys()):
        if s_dict[key] == 0:
            s_dict.pop(key)

    if s_dict:
        res += helper(s_dict)

    return res


print(reorganize('aab'))  # aba

"""
As you can see this approach works best for the given problem but it will not work for all the cases.
For example, if the input string is 'aaabc', the output will be 'abaca' but the correct output should be 'abaca' or 'acaba'.
"""

# negative test case
print(reorganize('aaabc'))  # abaca


def reorganize_queue(input_string):
    s_dict = Counter(input_string)
    s_dict = dict(sorted(s_dict.items(), key=lambda x: x[1], reverse=True))

    res = helper_queue(s_dict)

    for i in range(len(res) - 1):
        if res[i] == res[i + 1]:
            return ""
    return res


def helper_queue(s_dict):
    keys = list(s_dict.keys())
    res = ""
    for k, v in s_dict.items():
        if v > 0:
            res += k
            s_dict[k] -= 1
            break

    # if there is only one key left, we do not want to add it to the result string
    if len(keys) > 1:
        res += keys[-1]
        s_dict[keys[-1]] -= 1

    for k in keys:
        if s_dict[k] == 0:
            s_dict.pop(k)

    if s_dict:
        res += helper_queue(s_dict)

    return res


print(reorganize_queue('aaabc'))  # abaca or acaba
print(reorganize_queue('aaabcda')) # ""


"""
As you can see this approach works but isn't the best. The runtime is O(nlogn) but we use a lot of aux space.
We can do better.
"""

def reorganize_heap(input_string):
    s_dict = Counter(input_string)
    heap = [(-value, key) for key, value in s_dict.items()]
    heapq.heapify(heap)

    prev = None
    res = ""

    while heap or prev:
        if prev and not heap:
            return ""
        val, key = heapq.heappop(heap)
        res += key
        val += 1

        if prev:
            heapq.heappush(heap, prev)
            prev = None
        if val < 0:
            prev = (val, key)

    return res

reorganize_heap('aaabc')


