""" 
    Python utiliza el método de comparación lexicográfica para comparar cadenas. 
    Esto significa que los caracteres en la cadena se comparan uno por uno, 
    utilizando el orden ASCII. Si los caracteres son iguales, se pasará al siguiente 
    carácter. Si los caracteres son diferentes, el carácter con el código ASCII más 
    alto se considerará como la cadena mayor.

ejempĺo detallado en python

"apple" < "banana"
True

"apple" > "Banana"
True

En el primer ejemplo, la cadena "apple" es menor que la cadena "banana" porque 
la letra "a" en "apple" tiene un código ASCII más bajo que la letra "b" en "banana".

En el segundo ejemplo, la cadena "apple" es mayor que la cadena "Banana" porque 
la letra "a" en "apple" tiene un código ASCII más alto que la letra "B" en "Banana".

"""

print("apple" < "banana")
print("apple" > "Banana")

""" 
    La función de comparación de cadenas str.cmp() se ha eliminado en Python 3. 
    En su lugar, se recomienda usar la función built-in operator.eq(). 
    Esta función devuelve True si los dos argumentos son iguales, o 
    False si no lo son. 
    Sintaxis:
    
    import operator
    
    operator.eq(a, b)

    Parámetros: 
    a - Primer elemento para comparar. 
    b - Segundo elemento para comparar. 
"""

import operator

a = "Hello"
b = "World"

print(operator.eq(a, b)) # False