""" 
    Convertir los numeros impares del 0 al 30 en una lista y mostrarlos
"""

lista = list(range(1,30, 2))

for index in range(len(lista)):
    print(f"El indice {index} tiene el valor {lista[index]}")