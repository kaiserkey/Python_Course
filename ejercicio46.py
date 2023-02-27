""" 
    Funciones de listas
"""
lista_de_numeros = [1,2,3,4,5]
lista_de_colores = ['rojo', 'azul', 'amarillo', 'verde']
lista_de_palabras = ['gato', 'perro', 'caballo', 'elefante']
lista_heterogenea = [1, 'rojo', 'gato', 2, 'azul', 'perro', 3, 'amarillo', 'caballo', 4, 'verde', 'elefante', 5]

#1.	append() - Esta función se utiliza para agregar un elemento al final de la lista.
print(lista_de_numeros)
lista_de_numeros.append(6)
print(lista_de_numeros)

#1.1 insert() - Esta funcion inserta un elemento en la lista en la posicion elegida
print(lista_de_numeros)
lista_de_numeros.insert(0, 0)
print(lista_de_numeros)

#2.	extend() - Esta función se utiliza para agregar una lista a la lista actual.
print(lista_de_colores)
lista_de_colores.extend(["violeta", "naranja", "rojo"])
print(lista_de_colores)

#2.1 se puede concatenar listas con el operador +
print(lista_de_colores)
lista_concatenada = lista_de_colores + lista_de_palabras
print(lista_concatenada)

#3.	remove() - Esta función se utiliza para eliminar un elemento de la lista.
print(lista_de_palabras)
lista_de_palabras.remove("caballo")
print(lista_de_palabras)

#4.	pop() - Esta función se utiliza para eliminar el último elemento de la lista.
print(lista_heterogenea)
lista_heterogenea.pop()
print(lista_heterogenea)

#5.	index() - Esta función se utiliza para encontrar el índice de un elemento en la lista.
print(lista_de_colores.index("verde"))

#6.	count() - Esta función se utiliza para contar el número de veces que un elemento aparece en la lista.
print(lista_de_colores.count("rojo"))

#7.	sort() - Esta función se utiliza para ordenar los elementos de la lista.
print(lista_de_colores)
lista_de_colores.sort()
print(lista_de_colores)

#8.	reverse() - Esta función se utiliza para invertir los elementos de la lista.
print(lista_de_colores)
lista_de_colores.reverse()
print(lista_de_colores)

#9.	copy() - Esta función se utiliza para hacer una copia de la lista.
lista_de_colores_copy = lista_de_colores.copy()
print(lista_de_colores_copy)

#10. la repeticion de listas se puede hacer con el operador *
print(lista_de_colores * 5)

