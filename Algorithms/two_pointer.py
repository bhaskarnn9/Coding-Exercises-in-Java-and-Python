"""
find triplet that sum to 0
triplet([-1, -1, 1, 0, -1, 2, 3, -2])
the result should have non-repeating triplets
"""
from collections import Counter

def triplet(nums):
    nums.sort() # sorting the array enables us to skip duplicates
    res = set()
    for i in range(len(nums)):
       for j in range(i+1, len(nums)):
           for k in range(j+1, len(nums)):
               if nums[i] + nums[j] + nums[k] == 0:
                   res.add((nums[i], nums[j], nums[k]))
    return res


print(triplet([-1, -1, 1, 0, -1, 2, 3, -2]))

"""
the above is brute force using 0(n^3) time complexity
to improve this, we can use two loops as below
"""

def two_loop_triplet(nums):
    num_map = Counter(nums)
    nums.sort()
    res = set()
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            target = -(nums[i] + nums[j])
            if target in num_map and num_map[target] != i and num_map[target] != j:
                res.add((nums[i], nums[j], target)) if not combi((nums[i], nums[j], target), res) else None
                update_num_map(num_map, target)
    return res

def combi(combi, res): # check if the combination is already in the result
    for r in res:
        if Counter(r) == Counter(combi):
            return True
    return False

def update_num_map(num_map, target): # remove used target from the map, ensures no duplicates
    if num_map[target] > 1:
        num_map[target] -= 1
    else:
        num_map.pop(target) # remove the target from the map

print(two_loop_triplet([-1, -1, 1, 0, -1, 2, 3, -2]))

"""
the above is better using 0(n^2) time complexity
but we are using aux space Counter(r), Counter(combi), Counter(nums) and iterating through the result set O(k) where k is the length of the result set

This is the solution I implemented during one of my interviews.
On top of extra aux space, there's also a bug in the code:
{(-2, -1, 3), (-1, 2, -1), (-2, 0, 2), (-2, 1, 1)}
when target is 1 for pair -2, 1 I am finding an unexpected combination (-2, 1, 1) which should not be possible for the given input

Best approach is: We can use two pointers to solve this problem in 0(n^2) time complexity and 0(1) space complexity
"""

def two_pointer_triplet(nums):
    nums.sort()
    res = set()
    for i in range(len(nums)):
        left = i + 1
        right = len(nums) - 1
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            if total == 0:
                res.add((nums[i], nums[left], nums[right]))
                left += 1
                right -= 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    return res

print(two_pointer_triplet([-1, -1, 1, 0, -1, 2, 3, -2]))
