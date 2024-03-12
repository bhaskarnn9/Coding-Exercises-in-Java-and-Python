# SUMMER OF '69: Return the sum of the numbers in the array, except ignore sections of numbers starting with a 6 and 
# extending to the next 9 (every 6 will be followed by at least one 9). Return 0 for no numbers

import array as arr

def summer_69(input):
    
    my_array = arr.array('i', input)
    
    first_index_of_6 = my_array.index(6)

    first_index_of_9 = my_array.index(9)

    length_array = len(my_array)

    new_array = arr.array('i', [])

    x = 0
    while 1 > 0:
        if x == first_index_of_6:
            break
        else:
            new_array.append(my_array[x])
        x += 1
    
    y = first_index_of_9
    while 1 > 0:
        if y == length_array-1:
            break
        else:
            new_array.append(my_array[first_index_of_9])
        first_index_of_9 += 1
    
    print(sum(new_array))

summer_69([4, 5, 6, 7, 8, 9])

    