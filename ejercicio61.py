""" 
    Crear matriz con numpy e introducir numeros por el usuario
"""
import numpy as np

f = int(input("Ingrese el numero de filas: "))
c = int(input("Ingrese el numero de columnas: "))

M = np.empty((f,c), dtype=int)

print(f"==== Matriz de {f}x{c} ====")
for i in range(f):
    for j in range(c):
        M[i][j] = int(input("Ingrese un valor: "))

print(f"==== Matriz de {f}x{c} ====")
print(M)