""" 
    realizar la multiplicacion de dos matrices de 3x3
    
    Para poder multiplicar dos matrices, el numero de columnas de la primera matriz
    debe ser igual al numero de filas de la segunda matriz.
    y el resultado de la multiplicacion de dos matrices es una matriz de nxm
    la formula para cualquier matriz es:
    C[i][j] = A[i][0] * B[0][j] + A[i][1] * B[1][j] + A[i][2] * B[2][j]
"""

A = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
B = [[2, 3, 9], [5, 6, 2], [2, 2, 7]]

f = len(A)
c = len(A[0])



