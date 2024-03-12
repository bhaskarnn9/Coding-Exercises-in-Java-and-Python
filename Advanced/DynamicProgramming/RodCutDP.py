# def get_maximum_profit(price):
    
#     n = len(price)
#     if n <= 0:
#         return 0
    
#     table = [0]
#     table.extend(price)
        
    
#     for i in range(1, n+1):
#         profit = 0
#         for j in range(i):
#             temp = 0
#             temp = table[j] + table[i-j]
#             profit = max(profit, temp)
#         table[i] = profit
    
#     print(table)
#     return table[-1]

from typing import Deque
def get_maximum_profit(price):
    
    n = len(price)
    
    if n <= 0:
        return 0
    
    table = Deque() # start table for 0 cuts
    table.append(0)
    # table.extend(price) # append the prices for 1 - n cuts
    
    for i in range(1, n+1):
        max_revenue = 0
        for j in range(i):
            revenue = 0
            revenue = table[j] + price[i-2]
            max_revenue = max(revenue, max_revenue)
        table.append(max_revenue)
    print(table)
    return table[-1]

print(get_maximum_profit([3, 7, 8, 10, 12]))
