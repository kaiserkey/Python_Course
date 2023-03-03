""" 
    Crear manualmente una matriz de 4x4 y agregarle elementos
"""

M = [[0 for x in range(4)] for y in range(4)]

for i in range(len(M)):
    for j in range(len(M[0])):
        M[i][j] = int(input("Ingrese un valor: "))
        
for i in range(len(M)):
    for j in range(len(M[0])):
        print(M[i][j], end=" ")
    print()