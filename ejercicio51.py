""" 
    Dada una lista de caracteres, pedirle al usuario un elemento a eliminar de la lista.
"""

lista = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']

print(lista)

elemento = input("Ingrese un elemento a eliminar de la lista: ")

lista.remove(elemento.lower())

print(lista)