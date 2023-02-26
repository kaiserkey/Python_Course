""" 
    Hacer que el usuario introduzca numeros por neclado e ir sumandolos
    hasta que el usuario introduzca el numero 0
"""

suma = 0

numero = int(input("Introduce un numero: "))

while numero != 0:
    suma += numero
    numero = int(input("Introduce un numero: "))
else:
    print("La suma de los numeros es: ", suma)