import math

def solution(nums):
    max_subarray = -math.inf
    for i in range(len(nums)):
        current_subarray = 0
        for j in range(i, len(nums)):
            current_subarray += nums[j]
            max_subarray = max(max_subarray, current_subarray)
        
    return max_subarray

# solution([])


def sol(nums):

    subs = []

    for i in range(len(nums)):

        for j in range(1, len(nums)+1):

            subs.append(nums[i:j])
    
    print(subs)

# sol([1, 2, 3, 4, 5])
from collections import deque
def test(nums):
    lists = [[]]
    for i in range(len(nums) + 1): # 0, 1, 2, 3, 4, 5
        for j in range(i): # 0, 1, 2, 3, 4, 
            lists.append(nums[j: i])
    print(len(lists))
    return lists

num = ['a', 'b', 'c', 'd', 'e', 'f']


# print(test(num))

# print(2**6)


def get_subsets(nums):
    
    result = [[]]
    # result = [[], [a]]
    # result = [[], [a]] + [[b], [a, b]]

    
    for num in nums:
        for res in result:
            temp = []
            temp.append(res+[num])
            result = result + temp
            """
            above 3 lines is same as below one :
            result += [[num] + res for res in result]
            """
    print(result)

    # print('expected:', 2**len(nums), 'actual:', len(output))

    # print(output)

# get_subsets(['a', 'b', 'c', 'd', 'e'])
get_subsets(['super', 'highway', 'high', 'way'])




