from typing import List


class Solution:
    @staticmethod
    def majorityElement(nums: List[int]) -> int:

        res, count = 0, 0
        for n in nums:
            if count == 0:
                res = n
            count += (1 if n == res else -1)

        print('res', res)
        print('count', count)
        return res

s = Solution()
s.majorityElement([1,1,1,2,2,3,3])
s.majorityElement([0,0,1,1,1,1,2,3,3])