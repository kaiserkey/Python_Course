""" 
    realizar la division de dos matrices de 3x3
    
    para poder dividir dos matrices, deben ser del mismo tamaño y
    el resultado de la division de dos matrices es una matriz de nxm
    se debe dividir cada elemento de la primera matriz por cada 
    elemento de la segunda matriz
    la formula es C[i][j] = A[i][j] / B[i][j]
"""

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[2, 3, 9], [5, 6, 2], [2, 2, 7]]

f = len(A)
c = len(A[0])

if len(A) == len(B) & len(A[0]) == len(B[0]):
    C = [[0 for x in range(c)] for y in range(f)]
    
    for i in range(f):
        for j in range(c):
            C[i][j] = A[i][j] / B[i][j]

for 