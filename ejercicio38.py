""" 

    La función chr() en Python toma un número entero y devuelve una cadena 
    de caracteres Unicode que representa el carácter codificado con ese número 
    entero. Por ejemplo, chr(97) devolverá la cadena 'a'.

    La función ord() en Python toma una cadena de caracteres de longitud 1 y 
    devuelve su representación numérica Unicode. Por ejemplo, ord('a') devolverá 
    el número entero 97.

"""

n = int(input("Ingrese un número entero: "))
print(f"El carácter codificado para el número entero \"{n}\" ingresado es", chr(n))

s = input("Ingrese un caracter, longitud 1: ")
print(f"La representación numérica del caracter \"{s}\" ingresado es", ord(s))

