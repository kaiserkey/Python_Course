""" 
    Una matriz en Python se puede definir como una lista de listas. 
    Las listas anidadas representan a las filas de la matriz, mientras 
    que los elementos de cada lista individual representan las columnas.

    Por ejemplo, podemos definir una matriz de 3x3 como sigue:
"""
matriz = [[1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]]

"""
    Cada elemento de la matriz se puede acceder a través de su índice de fila y columna. 
    Por ejemplo, el elemento en la primera fila y segunda columna es igual a 2:
"""

print(matriz[0][1]) # devuelve 2

"""
    Para mostrar una matriz en Python, podemos simplemente iterar a través de cada fila y mostrar 
    los elementos en cada una. Por ejemplo, para mostrar la matriz anterior, usamos el siguiente código:
"""
for fila in matriz:
    for elemento in fila:
        print(elemento, end=' ')
    print()
    
"""
    El código anterior imprimirá la siguiente salida:

    1 2 3 
    4 5 6 
    7 8 9
"""
