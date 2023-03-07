""" 
    leer un string por teclado y devolver un diccionario con la cantidad de apariciones de cada caracter en el string
"""

myString = input("Ingrese una frase: ")

chars = list(myString)
dicc = {}

for char in myString:
    if char not in dicc:
        dicc[char] = 1
    else:
        dicc[char] += 1
print(dicc)