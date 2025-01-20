# LC:3009
# https://leetcode.com/problems/string-to-integer-atoi/

class Solution:
    def myAtoi(self, s: str) -> int:
        
        sign = 1 
        result = 0
        i = 0
        n = len(s)
        INT_MAX = pow(2,31) - 1 
        INT_MIN = -pow(2,31)

        while i < n and s[i] == ' ':
            i += 1
        
        if i < n and s[i] == '+':
            sign = 1
            i += 1
        elif i < n and s[i] == '-':
            sign = -1
            i += 1

        temp = ''
        while i < n and s[i].isdigit():
            digit = int(s[i])
            result = 10 * result + digit
            i += 1
        
        result = sign * result

        if result > INT_MAX:
            return INT_MAX
        elif result < INT_MIN:
            return INT_MIN
        else:
            return result

s = Solution()
print(s.myAtoi('-444444a00000'))