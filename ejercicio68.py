""" 
    leer un string por teclado y devolver un diccionario con la cantidad de apariciones de cada caracter en el string
"""

myString = input("Ingrese una frase: ")

chars = list(myString.upper())
dicc = {}

for char in chars:
    if char not in dicc and char != ' ':
        dicc[char] = chars.count(char)
        
print(myString.upper())
print(dicc)