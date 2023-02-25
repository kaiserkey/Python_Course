""" 
    Hacer un programa que resuelva ecuaciones de primer grado de la forma ax + b = 0 
    proporcionada por el usuario donde A != 0.
"""

A = float(input("Ingrese el valor de A: "))
B = float(input("Ingrese el valor de B: "))

if A != 0:
    print("La ecuación tiene solución: ", -B/A)
else:
    print("La ecuación no tiene solución.")