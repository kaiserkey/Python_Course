""" 
    Realizar la suma de dos matrices de 3x3
"""

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[2, 3, 9], [5, 6, 2], [2, 2, 7]]

f = len(A)
c = len(A[0])

if len(A) == len(B) & len(A[0]) == len(B[0]):
    C = [[0 for x in range(c)] for y in range(f)]
    
    for i in range(f):
        for j in range(c):
            C[i][j] = A[i][j] + B[i][j]
    print(C)