# """
# Cut The Rope

# Given a rope, cut it into parts maximizing the product of their lengths.

# Example
# Input: 4
# Output: 4

# Length of the rope is 4.
# All ways it can be cut into parts: 1+3, 1+1+2, 1+1+1+1, 2+2, 2+1+1.
# Among these, 2+2 cut makes for the greatest product: 2*2=4.

# Notes
# Input Parameters: Function has one argument, an integer length of the rope.

# Output Format: Return an integer, maximum possible product of the given rope’s parts.

# Constraints:
# 2 <= length of the rope <= 111
# You have to cut at least once.
# Length of the rope, lengths of all parts are all positive integers.

# JavaScript solutions will give “Wrong Answer” for the test cases from 023 to 029 because the answers exceed Number.MAX_SAFE_INTEGER. 
# If your JavaScript solution passes all the test cases except 023 to 029 and the latter tests your answers differ insignificantly, 
# conconsider your solution correct.

# Custom Input:
# Input Format: There should be only one line, containing an integer n, denoting length of rope. If n = 5, then input should be: 5

# Output Format: There will be one line, containing an integer maxProduct. For input n = 5, output will be:
# 6
# """

# # def max_prod(n):
    
# #     # base cases
# #     # if len of rope = 0, no cuts are possible, therefore product = 0
# #     # if len of rope = 1, no cuts are possible, therefore product = 0
# #     if n <= 1:
# #         return 0
# #     # if len of rope = 2, we can cut such rope in only one way = [1, 1]
# #     if n == 2:
# #         return 1
    
# #     # initialize cache/table for DP
# #     cache = [0 for x in range(n+1)] # n + 1 because we want to include n
# #     # cache looks like [0, 0, 0, 0, 0]
# #     # put values of 0, 1 and 2 cuts in the table
# #     cache[1] = 0
# #     cache[2] = 1
# #     # now cache looks like [0, 0, 1, 0, 0]
    
# #     for l in range(3, n+1): # 0, 1, 2, are alraedy addressed and let's address from 3 to n
# #         for cut in range(1, l): # Possibilities of 3 are 1 + 2
# #             # print(f'cache[{l}]', cache[l])
# #             cache[l] = max(cache[l], max(cut*(l-cut), cut*cache[l-cut]))
# #     return cache[-1]

# def max_prod(n):
    
#     # base cases
#     # if len of rope = 0, no cuts are possible, therefore product = 0
#     # if len of rope = 1, no cuts are possible, therefore product = 0
#     if n <= 1:
#         return 0
#     # if len of rope = 2, we can cut such rope in only one way = [1, 1]
#     if n == 2:
#         return 1
    
#     # initialize cache/table for DP
#     cache = [0 for x in range(n+1)] # n + 1 because we want to include n
#     # cache looks like [0, 0, 0, 0, 0]
#     # put values of 0, 1 and 2 cuts in the table
#     cache[1] = 0
#     cache[2] = 1
#     # now cache looks like [0, 0, 1, 0, 0]

#     for l in range(3, n+1): # 0, 1, 2, are alraedy addressed and let's address from 3 to n
#         max_val = 0
#         for cut in range(1, l): # Possibilities of 3 are 1 + 2
#             product = cache[cut]*cache[l-cut]
#             max_val = max(max_val, product)
#         cache[l] = max_val
    
#     return cache[-1]

# print(max_prod(4))


MAX_CHAR = [26]


print(MAX_CHAR)







