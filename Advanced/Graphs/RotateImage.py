from typing import Deque
import numpy as np

def create_matrix(n):
    mat_input = [i for i in range(1, n*n+1)]
    splits = np.array_split(mat_input, n)
    mat_input = []
    for split in splits:
        mat_input.append(list(split))
    
    print(np.matrix(mat_input))
    solution(mat_input)

def solution(input_matix):

    rows, cols = len(input_matix), len(input_matix[0])
    n = rows * cols
    top = 0
    bottom = rows-1
    left = 0
    right = cols-1

    while left < right:

        de = Deque()

        # traverse left to right and store values
        for col in range(left, right+1):
            de.append(input_matix[top][col])
        
        # traverse top to bottom and replace values
        for row in range(top, bottom+1):
            de.append(input_matix[row][right])
            curr = de.popleft()
            input_matix[row][right] = curr
            
        right-=1
        de.popleft()
        print(np.matrix(input_matix))

        # traverse right to left and replace values
        for col in range(right, left-1, -1):
            de.append(input_matix[bottom][col])
            curr = de.popleft()
            input_matix[bottom][col] = curr
            
        bottom-=1
        print(np.matrix(input_matix))
        
        # traverse bottom to top and replace values
        for row in range(bottom, top-1, -1):
            de.append(input_matix[row][left])
            curr = de.popleft()
            input_matix[row][left] = curr
            
        left+=1
        print(np.matrix(input_matix))
        
        # traverse left to right and store values
        for col in range(left, right+1):
            curr = de.popleft()
            input_matix[top][col] = curr
            
        top+=1
        print(np.matrix(input_matix))

    return input_matix

create_matrix(5)



