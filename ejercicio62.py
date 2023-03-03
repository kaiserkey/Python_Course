""" 
    realizar la multiplicacion de dos matrices con numpy
"""
import numpy as np

f = int(input("Ingrese el numero de filas de la matriz A: "))
c = int(input("Ingrese el numero de columnas de la matriz A: "))
cb = int(input("Ingrese el numero de columnas de la matriz B: "))

A = np.empty((f,c), dtype=int)
B = np.empty((c,cb), dtype=int)
C = np.zero((f,cb), dtype=int)

