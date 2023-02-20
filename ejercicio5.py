""" Podemos saber el tipo de dato de una variable con la funcion type() """

miNumero = 15
miTexto = "Hola Mundo"
miBooleano = True
miFlotante = 3.14
miFlotante2 = 3.0
miFlotante3 = 3.

print(type(miNumero))
print(type(miTexto))
print(type(miBooleano))

""" Podemos convertir un tipo de dato a otro """

print(int(miFlotante)) #!Cuidado porque se pierde la parte decimal

""" Al realizar operaciones con numeros decimales el resultado es un numero decimal """

print(type(miFlotante3 + miNumero))

