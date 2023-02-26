""" 
    Dado un string calcular el numero de vocales que tiene.
"""

texto = "lorem ipsum dolor sit ameta"
texto = texto.lower()
print(texto)

count = 0
repeticiones = 0

while repeticiones < len(texto):
    if texto[repeticiones] == "a" or texto[repeticiones] == "e" or texto[repeticiones] == "i" or texto[repeticiones] == "o" or texto[repeticiones] == "u":
        count += 1
    repeticiones += 1

print("El numero de vocales es: ", count)