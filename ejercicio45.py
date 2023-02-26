""" 
    Estructuras de datos en python

    Python ofrece una gran variedad de estructuras de datos. Estas son algunas de las estructuras 
    de datos más comunes en Python:

    1. Listas: una lista es una colección ordenada y mutable de elementos. Las listas se pueden 
    modificar al agregar, eliminar o reemplazar elementos.

    2. Tuplas: una tupla es una colección ordenada e inmutable de elementos. Las tuplas no se 
    pueden modificar una vez creadas.

    3. Conjuntos: un conjunto es una colección desordenada e inmutable de elementos únicos. Los 
    conjuntos no se pueden modificar una vez creados.

    4. Diccionarios: un diccionario es una colección desordenada de pares clave-valor. Los diccionarios 
    se pueden modificar al agregar, eliminar o reemplazar elementos.

    5. Matrices: una matriz es una colección ordenada de elementos. Las matrices se pueden modificar al 
    agregar, eliminar o reemplazar elementos.

    Ejemplos de algunas estructuras de datos en Python:

    Lista: [1, 2, 3, 4, 5]
    Tupla: (1, 2, 3, 4, 5) //no modificable
    Conjunto: {1, 2, 3, 4, 5} // no modificable
    Diccionario: {'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
    Matriz: [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
"""

lista_de_numeros = [1,2,3,4,5]
lista_de_colores = ['rojo', 'azul', 'amarillo', 'verde']
lista_de_palabras = ['gato', 'perro', 'caballo', 'elefante']
lista_heterogenea = [1, 'rojo', 'gato', 2, 'azul', 'perro', 3, 'amarillo', 'caballo', 4, 'verde', 'elefante', 5]

""" 
    Formas de imprimir una lista en python
"""
# usando el metodo print
print(lista_de_numeros)
print(lista_de_colores)
print(lista_de_palabras)
print(lista_heterogenea)

# usando el ciclo for
for elemento in lista_de_colores:
    print(elemento)
    
# usando la funcion enumerate()
for indice, elemento in enumerate(lista_de_palabras):
    print(f"Indice -> {indice} - Elemento -> {elemento}")
    
# usando la funcion list.index()
for indice in range(len(lista_de_numeros)):
    print(f"Indice -> {lista_de_numeros.index(indice+1)} - Elemento -> {lista_de_numeros[indice]}")
