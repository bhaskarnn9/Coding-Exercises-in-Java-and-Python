import numpy as np

"""
[[0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]
 [0 0 0 0 0 0 0 0 0 0]]
 """


def spiral(n):
    
    matrix = [[0 for _ in range(n)] for _ in range(n)]


    rl, rr, ct, cb = 0, n-1, 0, n-1  # boundaries of the matrix
    x = 1

    while rl <= rr and ct <= cb:  # while the boundaries are valid
        
        for i in range(rl, rr + 1): # fill the top row
            matrix[rl][i] = x
            x += 1
        ct += 1

        for i in range(ct, cb + 1): # fill the right column
            matrix[i][rr] = x
            x += 1
        rr -= 1

        if ct <= cb:
            for i in range(rr, rl - 1, -1): # fill the bottom row
                matrix[cb][i] = x
                x += 1
            cb -= 1

        if rl <= rr:
            for i in range(cb, ct -1, -1):  # fill the left column
                matrix[i][rl] = x
                x += 1
            rl += 1

    print(np.array(matrix))  # just for matrix visualization

spiral(3)
