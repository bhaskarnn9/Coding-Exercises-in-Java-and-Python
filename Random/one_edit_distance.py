# LC: 161
# https://leetcode.com/problems/one-edit-distance

class Solution:
    def isOneEditDistance(self, s: str, t: str) -> bool:

        if s == t:
            return False
        
        ns = len(s)
        nt = len(t)

        # make sure s is shorter
        if ns > nt:
            return self.isOneEditDistance(t, s)

        if nt - ns > 1:
            return False

        for i in range(ns):

            if s[i] != t[i]:
                if ns == nt:
                    return s[i + 1:] == t[i + 1:]
                else:
                    return s[i:] == t[i + 1]
            
        return ns + 1 == nt


s = Solution()
# +ve
print(s.isOneEditDistance('a', 'ab'))
print(s.isOneEditDistance('', 'a'))
print(s.isOneEditDistance('xzy', 'xxy'))
#-ve
print(s.isOneEditDistance('aaa', 'ab'))
print(s.isOneEditDistance('', 'ab'))
print(s.isOneEditDistance('xxx', 'x'))