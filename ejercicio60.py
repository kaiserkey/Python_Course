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

print
# crear una matriz nula con los mismos valores de la matriz M
B_like_M = np.zeros_like(M)

for i in range(len(B_like_M)):
    for j in range(len(B_like_M[0])):
        print(B_like_M[i][j], end=" ")
    print()


