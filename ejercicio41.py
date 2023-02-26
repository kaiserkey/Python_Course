""" 
    Escribir un programa  que imprima los numeros del 1 al 10 y su cubo
"""
import math as mt
for i in range(1,11):
    print(f"El numero {i} elevado al cubo es: {mt.pow(i,3)}")
else:
    print("Fin del programa")