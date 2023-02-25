""" 
Los operadores de desicion en python son:

-Operador if: este operador evalúa una condición y ejecuta un bloque de código si la condición es verdadera.
-Operador else: este operador se usa junto con el operador if para proporcionar una alternativa si la condición evaluada por el operador if es falsa.
-Operador elif: este operador se usa con el operador if para proporcionar otra condición que se puede evaluar si la condición original del operador if es falsa.
-Operador de comparación: estos operadores se usan para comparar dos valores y determinar si son iguales, mayores o menores. Los operadores de comparación comunes son ==, !=, >, <, >= y <=.
== : Esta operación es un operador de comparación que verifica si dos valores son iguales.
!=: Esta operación también es un operador de comparación, pero en lugar de verificar si dos valores son iguales, verifica si dos valores son diferentes.
>: Esta operación es una comparación de mayor que, que verifica si un valor es mayor que otro.
<: Esta operación es una comparación de menor que, que verifica si un valor es menor que otro.
>=: Esta operación es una comparación de mayor o igual que, que verifica si un valor es mayor o igual que otro.
<=: Esta operación es una comparación de menor o igual que, que verifica si un valor es menor o igual que otro.

Ejemplos practicos
"""

# Ejemplo 1

num1 = 10
num2 = 5

if num1 > num2:
    print("num1 es mayor que num2")

# Resultado: num1 es mayor que num2

# Ejemplo 2

num1 = 10
num2 = 15

if num1 > num2:
    print("num1 es mayor que num2")
else:
    print("num2 es mayor que num1")

# Resultado: num2 es mayor que num1

# Ejemplo 3

num1 = 10
num2 = 10

if num1 == num2:
    print("num1 es igual que num2")
else:
    print("num2 no es igual que num1")

# Resultado: num1 es igual que num2

# Ejemplo 4

num1 = 1
num2 = 10

if num1 != num2:
    print("num1 es distinto de num2")
else:
    print("num2 no es distinto de num1")

# Resultado: num2 es distinto de num1