""" 
    Dado un string, con un bucle for, vamos a imprimirlo sin vocales y vamos a salir del bucle si la letra que 
    indique el usuario aparece mas de n veces.
"""

texto = "lorem ipsum dolor sit amet"
texto = texto.lower()
print(texto)

letra = str(input("Ingresa una letra: "))
letra = letra.lower()

contador = int(input("Ingresa el numero de veces que quieres que aparezca la letra: "))

for i in texto:
    if i == letra:
        contador = contador - 1
        if contador == 0:
            break

    if(i == "a" or i == "e" or i == "i" or i == "o" or i == "u"):
        continue
    
    print(i, end="")
    
print()
