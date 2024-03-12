prices = [2, 5, 7, 9, 11]

def solution(prices):
    if len(prices) <= 0:
        return 0
    
    new_prices = [0]
    [0, 2, 5, 7, 9, 11]
    
    new_prices.extend(prices)
    
    for i in range(2, len(prices)):
        print('loop1: i', i)
        profit = 0
        for j in range(0, i//2 + 1):
            temp = 0
            temp = new_prices[j] + new_prices[i-j]
            print(f'new_prices[{j}]={new_prices[j]}', f'+ new_prices[{i-j}]={new_prices[i-j]}')
            profit = max(profit, temp)
            print('profit', profit)
        new_prices[i] = profit
    
    return new_prices[len(prices)]




solution(prices)


