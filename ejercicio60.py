""" 
    Matrices con Nunpy 
"""

import numpy as np

# crear matriz vacia
M = np.empty((3,3), dtype=int)

#crear una matriz nula
M = np.zeros((3,3), dtype=int)

for i in range(len(M)):
    for j in range(len(M[0])):
        print(M[i][j], end=" ")
    print()
print()
# crear una copia de la matriz
copy_M = M.copy()

for i in range(len(copy_M)):
    for j in range(len(copy_M[0])):
        print(copy_M[i][j], end=" ")
    print()

print()
# crear una matriz nula con los mismos valores de la matriz M
B_like_M = np.zeros_like(M)

for i in range(len(B_like_M)):
    for j in range(len(B_like_M[0])):
        print(B_like_M[i][j], end=" ")
    print()
print()

# crear una matriz de unos 
E = np.ones((3,3), dtype=int)

for i in range(len(E)):
    for j in range(len(E[0])):
        print(E[i][j], end=" ")
    print()
print()

# crear una matriz de unos con los mismos dimensiones de la matriz M
E_like_M = np.ones_like(M)

for i in range(len(E_like_M)):
    for j in range(len(E_like_M[0])):
        print(E_like_M[i][j], end=" ")
    print()
print()

# para saber las dimenciones de una matriz
print(M.shape, "filas y columnas")

# para saber el tipo de dato de una matriz
print(M.dtype, "tipo de dato")

# sumar dos matrices
A = np.matrix([ [1,2,3],
                [4,5,6],
                [7,8,9] ])

B = np.matrix([ [3,5,1],
                [7,8,4],
                [4,2,4] ])

print(A+B)

# para multiplicar dos matrices
print(A.dot(B))