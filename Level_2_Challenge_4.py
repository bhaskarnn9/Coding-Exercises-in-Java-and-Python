# Given a list of ints, return True if the array contains a 3 next to a 3 somewhere.

import array as arr

def has_33(nums):
    input_list = nums

    my_array = arr.array('i', input_list)
    try:
        index = my_array.index(3)
    except ValueError:
        print('There\'s no 3 in the array')
        exit()

    next_number = my_array[index+1]
    if next_number == 3:
        return True
    else:
        return False
    

print(has_33([2, 5, 1, 3, 0, 3]))