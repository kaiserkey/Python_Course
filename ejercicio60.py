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

# crear una copia de la matriz
copy_M = M.copy()

for i in range(len(copy_M)):
    for j in range(len(copy_M[0])):
        print(copy_M[i][j], end=" ")
    print()