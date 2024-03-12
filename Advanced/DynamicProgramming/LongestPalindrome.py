"""
Given a string s, return the longest palindromic substring in s

Example 1:

Input: s = "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

Example 3:

Input: s = "a"
Output: "a"

Example 4:

Input: s = "ac"
Output: "a"
"""

# def test():
#     x = 'salim'
#     for i in range(1, len(x)+1):
#         print(i, x[:i])

# test()

import heapq

'abac'

def solution(s):

    res = ''

    for i in range(len(s)):

        for j in range(1, len(s)+1):
            
            if len(s[i:j]) < 1:
                continue

            if check_palindrome(s[i:j]):
                res = max(res, s[i:j], key=len)
    
    print(res)



def grow(s):
    biggest = s[0]
    step = len(biggest)// 2

    # handle odd length words
    for center in range(1, len(s)-1):
        bounds = [center-(step+1), center+(step+1)]
        while bounds[0] > -1 and bounds[1] < len(s):
            if check_palindrome(s[bounds[0]:bounds[1]+1]):
                biggest = s[bounds[0]:bounds[1]+1]
                step = len(biggest)//2
                bounds[0] -= 1
                bounds[1] += 1
            else:
                break
    
    print(biggest)
    
    # handle even length words
    for center in range(step, len(s)-step-1):
        bounds = [center-step, center+(step+1)]
        while bounds[0] > -1 and bounds[1] < len(s):
            if check_palindrome(s[bounds[0]:bounds[1]+1]):
                biggest = s[bounds[0]:bounds[1]+1]
                step = len(biggest)//2
                bounds[0] -= 1
                bounds[1] += 1
            else:
                break

    print(biggest)


def check_palindrome(s):
    if len(s) == 1:
        return True
    x = ''.join(reversed(s))
    return x == s

grow('lleh')