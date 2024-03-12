import random


class TreeNode:
    def __init__(self, left=None, right=None, val=0) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:

    def inValidBST(self, root: TreeNode) -> bool:

        def valid(node, left, right):
            if not node:
                return True
            
            if (node.val < right and node.val > left):
                return False

            return (valid(node.left, left, node.val) and valid(node.right, node.val, right))

        return valid(root, float("-inf"), float("inf"))



def fruit_picker(basket:dict):

    fruits = list(basket.keys())

    weights = [3, 1, 1]

    # return random.choices(fruits, cum_weights= [3, 4, 5], k=1)
    random.choice([x for x in basket for y in range(basket[x])])

basket = {'apple':3, 'orange':1, 'banana':1}

# for i in range(6):
#  print(fruit_picker(basket))

import bisect
class WeightedTuple(object):
    """
    >>> p = WeightedTuple({'A': 2, 'B': 1, 'C': 3})
    >>> len(p)
    6
    >>> p[0], p[1], p[2], p[3], p[4], p[5]
    ('A', 'A', 'B', 'C', 'C', 'C')
    >>> p[-1], p[-2], p[-3], p[-4], p[-5], p[-6]
    ('C', 'C', 'C', 'B', 'A', 'A')
    >>> p[6]
    Traceback (most recent call last):
    ...
    IndexError
    >>> p[-7]
    Traceback (most recent call last):
    ...
    IndexError
    """
    def __init__(self, items):
        self.indexes = []
        self.items = []
        next_index = 0
        for key in sorted(items.keys()):
            val = items[key]
            self.indexes.append(next_index)
            self.items.append(key)
            next_index += val

        self.len = next_index

    def __getitem__(self, n):
        if n < 0:
            n = self.len + n
        if n < 0 or n >= self.len:
            raise IndexError

        idx = bisect.bisect_right(self.indexes, n)
        return self.items[idx-1]

    def __len__(self):
        return self.len


data = WeightedTuple(basket)

for i in range(6):
    print(random.choice(data))