""" 
    Escriba un programa que imprima la suma de los números pares del 2 al 20
"""
suma = 0
for i in range(1, 20):
    if i % 2 == 0:
        suma += i
else:
    print("La suma de los numeros pares es: ", suma)