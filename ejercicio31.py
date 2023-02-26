""" 
    Crear un bucle que imprima todas las letras de una frase excepto
    la letra ingresada por el usuario
"""

texto = "lorem ipsum dolor sit amet"

letra = str(input("Ingresa una letra que no quieres que se imprima:"))

for i in range(0, len(texto)):
    if texto[i] == letra:
        continue
    else: 
        print(texto[i], end="")

print()