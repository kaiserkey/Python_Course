""" 
    Matrices con Nunpy 
"""

import numpy as np

# crear matriz vacia
M = np.empty((3,3), dtype=int)

for i in range(len(M)):
    for j in range(len(M[0])):
        print(M[i][j])