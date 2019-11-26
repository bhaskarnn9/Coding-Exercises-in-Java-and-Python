# Function Practice Exercises

'''
Write a function that reeturns the lesser of two given numbers if both numbers
are even, but returns the gerater if one or both numbers are odd
'''

def return_even_or_odd(a, b):
    if a % 2 == 0 and b % 2 == 0:
        return min(a,b)
    else:
        return max(a, b)


print(return_even_or_odd(1, 4))
