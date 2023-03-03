""" 
    realizar la multiplicacion de dos matrices con numpy
"""
import numpy as np

f = int(input("Ingrese el numero de filas de la matriz A: "))
c = int(input("Ingrese el numero de columnas de la matriz A: "))
cb = int(input("Ingrese el numero de columnas de la matriz B: "))

A = np.empty((f,c), dtype=int)
B = np.empty((c,cb), dtype=int)
C = np.zeros((f,cb))

print(f"==== Matriz A de {f}x{c} ====")
for i in range(f):
    for j in range(c):
        A[i][j] = int(input(f"Ingrese un valor para [{i},{j}]: "))

print(f"==== Matriz B de {c}x{cb} ====")
for i in range(c):
    for j in range(cb):
        B[i][j] = int(input(f"Ingrese un valor para [{i},{j}]: "))

C = A * B

print(f"==== Matriz C de {f}x{cb} ====")
print(C)