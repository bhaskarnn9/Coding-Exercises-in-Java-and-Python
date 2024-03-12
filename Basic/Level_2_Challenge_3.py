"""
BLACKJACK: Given three integers between 1 and 11, if their sum is less than or equal to 21, 
return their sum. If their sum exceeds 21 and there's an eleven, reduce the total sum by 10. 
Finally, if the sum (even after adjustment) exceeds 21, return 'BUST'
"""

def BLACKJACK(a, b, c):
    input = [a, b, c]
    sum_input = sum(input)
    if sum_input is 21 or sum_input < 21:
        return sum_input
    elif sum_input > 21 and 11 in input:
        return sum_input - 10
    else:
        return 'BUST'

print(BLACKJACK(9,10,9))
    

