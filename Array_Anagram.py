"""
Anagram check
Given two strings, check to see if they are anagrams.
Anagram : When the two strings can be written using the exact the same letters
(so you can just rearrange the letters to get a different phrase or word), it is an anagram.

Example: 'public relations" is an anagram of 'crap built on lies.'
"""
from array import *


def anagram(s1, s2):
    # remove spaces, and lower all the characters
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    print(s1)
    print(s2)

    sorted_s1 = sorted(s1)
    sorted_s2 = sorted(s2)

    print(sorted_s1)
    print(sorted_s2)

    return sorted_s1 == sorted_s2


def anagram2(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    # Edge case check - no of characters

    if len(s1) != len(s2):
        print('returning false')
        return False

    count = {}

    for char in s1:
        if char in count:
            count[char] += 1
        else:
            count[char] = 1

    print(count)

    for char in s2:
        if char in count:
            count[char] -= 1
        else:
            count[char] = 1

    print(count)

    for k in count:
        if count[k] != 0:
            return False

    return True


def anagram3(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        print('returning false')
        return False

    list_s1 = []
    for char in s1:
        if char not in list_s1:
            list_s1.append(char)
    print(list_s1)

    list_s2 = []
    for char in s2:
        if char not in list_s2:
            list_s2.append(char)
    print(list_s2)

    if len(list_s1) != len(list_s2):
        return False

    return True


print(anagram3('tomato o', 'at mo too'))