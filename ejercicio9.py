""" 
    Numeros Complejos: es un numero que se puede expresar como la suma de un numero real y un numero imaginario
    z = a + bi con a y b numeros reales y i = sqrt(-1)
    Parte Real: es el primer numero de la suma, Re(z) = a
    Parte Imaginaria: es el segundo numero de la suma, Im(z) = b
    Complejo Real: es un numero que solo tiene parte real, Im(z) = 0
    Imaginario Puro: es un numero que solo tiene parte imaginaria, Re(z) = 0
    Unidad Imaginaria: es el numero i = sqrt(-1)
    Conjunto de nuemros complejos: es el conjunto de todos los numeros complejos C= {z = a + bi | a,b E R}

    Suma: z1 + z2 = (a1 + a2) + (b1 + b2)i
    Resta: z1 - z2 = (a1 - a2) + (b1 - b2)i
    Producto: z1 * z2 = (a1 * a2 - b1 * b2) + (a1 * b2 + a2 * b1)i
    Division: z1 / z2 = (a1 * a2 + b1 * b2) / (a2^2 + b2^2) + ((a2 * b1 - a1 * b2) / (a2^2 + b2^2))i
"""

# En Python los numeros complejos se representan con la letra j en vez de i

z1 = 1 + 7j
z2 = complex(4, 6)

print(type(z1))
print(z2)

# Obtener la parte real de un numero complejo y la parte imaginaria
print(z1.real)
print(z1.imag)

print("Suma (1 + 7j) + (4 + 6j) ->", z1+z2)
print("Resta (1 + 7j) - (4 + 6j) ->",z1-z2)
print("Multiplicacion (1 + 7j) * (4 + 6j) ->",z1*z2)
print("Division (1 + 7j) / (4 + 6j) ->",z1/z2)

