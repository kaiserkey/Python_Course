""" 
    Operadores de iteracion:
    While: El bucle while es otra de las estructuras de control de iteración 
    más utilizadas en Python. Su sintaxis es:
    
    while condición:
      -Haz algo

    El ciclo de ejecucion while se seguira ejecutando siempre y cuando se cumpla 
    la condición especificada, hasta que esta se viole y el ciclo se termine. Si
    la condicion nunca es modificada para que sea falsa, el ciclo se ejecutara
    de manera infinita.
    
    Se puede usar la función print() con el argumento opcional "end" para imprimir sin saltar de línea.

    Ejemplo:

    print("Hola", end=" ")
    print("Mundo")

    Salida:
    Hola Mundo
"""

#Ejemplo
numero = 0

while numero < 10:
  print(numero+1, end=" ")
  numero += 1
  
print()
