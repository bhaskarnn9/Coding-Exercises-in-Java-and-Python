from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    @staticmethod
    def addTwoNumbers(l1: Optional[ListNode], l2: Optional[ListNode]):
        res = 0

        temp = ''
        current = l1
        while current:
            temp += str(current.val)
            current = current.next


        res += int(temp[::-1])

        temp = ''
        current = l2
        while current:
            temp += str(current.val)
            current = current.next

        res += int(temp[::-1])

        r = []
        for c in str(res):
            r.append(int(c))
        return r[::-1]


"""
Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
"""

def get_list_node(list_l):
    l = None
    current = None

    for n in list_l:
        new_node = ListNode(n)
        if l is None:
            l = new_node
            current = l
        else:
            current.next = new_node
            current = current.next
    return l

l1 = get_list_node([2, 4, 3])
l2 = get_list_node([5, 6, 4])


s = Solution()
print(s.addTwoNumbers(l1, l2))
