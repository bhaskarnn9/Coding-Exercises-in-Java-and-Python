def coin_change(arr, len, target):
    
    # if the target is 0, there's only one way and that is []
    if target == 0:
        return 1

    # if the target is 0, there's no way to add up to target with +ve integers
    if target < 0:
        return 0
    
    # if the target not 0 but we have no coins, we cannot add up to target
    if len <= 0 and target > 0:
        return 0
    
    # We have two possible ways to add up
    # 1: calculate change for target : 0, 1, 2....target --> (arr, len, target-arr[len-1])
    # 2: calculate change with coins : 0, 1, 2....len

    return coin_change(arr, len-1, target) + coin_change(arr, len, target-arr[len-1])



print(coin_change([1, 2, 3], 3, 4))