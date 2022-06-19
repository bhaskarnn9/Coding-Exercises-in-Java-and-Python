from collections import deque
from operator import le


nums = [205, 321, 190, 180, 48, 110, 148, 83, 469, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15 ,36, 193, 115, 209, 38, 24, 113, 424, 230, 463, 271, 398, 434, 19, 471, 
489, 449, 368, 212, 307, 76, 467, 34, 333, 412, 459, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 234, 286, 22, 7, 146, 141, 192, 323, 367, 81, 414, 443, 68, 392, 370, 
309, 152, 133, 413, 89, 118, 332, 365, 92, 482, 127, 11, 52, 411, 119, 2, 473, 138, 441, 174, 64, 74, 401, 35, 95, 18, 227, 
54, 289, 317, 396, 20, 322, 372, 360, 130, 70, 447, 451, 163, 394, 295, 223, 458, 287, 116, 366, 123, 348, 140, 1 ,8 ,7 ,6 ,5 ,4 ,3 ,2 ,1]

def longest_sequence(nums):

    longest_sequence = []

    for i in range(1, len(nums)):
        seq = deque()
        if nums[i] == nums[i-1] + 1:
            seq.appendleft(nums[i-1])
        else:
            continue

        while nums[i] == nums[i-1] + 1:
            if i == len(nums):
                break
            seq.append(nums[i])
            i += 1
        
        if len(longest_sequence) < len(seq):
            longest_sequence = seq

    
    print(longest_sequence)
    return longest_sequence

longest_sequence(nums)



