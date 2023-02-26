""" 
    Escribir las tablas de multiplicar del 1 al 10 anidando dos bucles for.
"""

for i in range(1, 11):
    print()
    print("Tabla del ", i)
    for j in range(1, 11):
        print(f"{i} x {j} = {(i)*(j)}")