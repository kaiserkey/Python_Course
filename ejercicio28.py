""" 
    For: El bucle for es una de las estructuras de control de iteración más 
    utilizadas en Python. Su sintaxis es:

    for elemento in secuencia:
        --Haz algo con elemento
        
    El ciclo for se ejecuta un número específico de veces, es decir, se ejecuta 
    una cantidad determinada de veces, sin importar si se cumple o no la condición.
    
    For in Range: El for in range es un bucle que itera sobre una secuencia de números. 
    Está diseñado para iterar sobre un rango de números, comenzando en cero y terminando 
    en un número específico. Su sintaxis es:

    for x in range(inicio, fin, incremento):
        --Haz algo con x
"""

# Ejemplo: Imprimir los números del 1 al 10
for i in range(10):
    print(i+1, end=" ")
    
print()

# Ejemplo: Imprimir los números del 10 al 20
for i in range(10, 20):
    print(i, end=" ")
    
print()

# Ejemplo: Imprimir los números del 0 al 10 con incremento de 2
for i in range(0, 10, 2):
    print(i, end=" ")
    
print()

