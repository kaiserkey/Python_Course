""" 
    Crear matriz con numpy e introducir numeros por el usuario
"""
import numpy as np



M = np.empty((4,4), dtype=int)

print("Matriz de 4x4")
for i in range(len(M)):
    for j in range(len(M[0])):
        M[i][j] = int(input("Ingrese un valor: "))
