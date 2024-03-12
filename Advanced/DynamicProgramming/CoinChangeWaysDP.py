def coin_change(A, len, target):

    table = [[0 for x in range(len)] for x in range(target + 1)]
    
    print(table)

    for i in range(len):
        table[0][i] = 1
    
    print(table)

    for i in range(1, target+1):
        for j in range(len):

            x = table[i - A[j]][j] if i-A[j] >= 0 else 0
            y = table[i][j-1] if j >= 1 else 0
            table[i][j] = x + y
    
    print(table)
    return table[target][len-1]

print(coin_change([1, 2, 3], 3, 4))
