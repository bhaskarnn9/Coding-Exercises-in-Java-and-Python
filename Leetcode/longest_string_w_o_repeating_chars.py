from collections import deque


s = 'ckilbkd'
def longest(s):
    longest = []
    temp = None
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            continue
        else:
            temp = str(s[i-1])
        
        while s[i] != s[i-1]:
            if s[i] not in temp:
                temp = temp + s[i]
            else:
                break
            i += 1
            if i == len(s):
                break
        
        longest.append(temp)
    
    longest = sorted(longest, key=len, reverse=True)[:1]
    if not longest:
        return len(s[0])
    print(longest[0])
    return len(longest[0])

print(longest(s))
