""" 
    Strings: cadena de caracteres
    Una variable de tipo string se puede definir con comillas simples o dobles
"""

texto1 = "Esto es un string entre comillas dobles"
texto2 = 'Esto es un string entre comillas simples'

print(type(texto1))
print(type(texto2))

texto3 = "Esto es un string con comillas dobles \" dentro del string y comillas simples 'dentro del string'"

print(texto3)

""" 
    En python los acentos se pueden usar sin problemas
    Pero pueden generar problemas en distintos sistemas operativos
"""

print("Cadena con acento: áéíóú")

""" 
    String literal: es un string que se define para ser usado en multiples lineas y se define con tres comillas simples o dobles
    \n: es un caracter de escape que representa un salto de linea
    \t: es un caracter de escape que representa un tabulador
    \\: es un caracter de escape que representa una barra invertida
    \': es un caracter de escape que representa una comilla simple
    \": es un caracter de escape que representa una comilla doble
"""

stringLiteral = """
                    Esto es un string literal
                    que se define con tres comillas dobles
                    o simples
                """

stringFrase = "Esto es un string literal \n que tiene un salto de linea \t y un tabulador"
print(stringFrase)

stringFrase2 = "John McCarthy Dijo: \"Los algoritmos son la combinación perfecta de matemáticas, lógica y creatividad.\""
print(stringFrase2)

""" 
    Concatenacion de strings: es la union de dos o mas strings
    En python se puede concatenar strings con el operador +
"""

primeraParte = "Esto es la primera parte del string " # Recordar colocar un espacio en blanco al final del string
segundaParte = "- Esto es la segunda parte del string"
print(primeraParte + segundaParte)

