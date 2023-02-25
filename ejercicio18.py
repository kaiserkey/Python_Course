""" 
Template string en Python es una característica de la sintaxis que permite 
la fácil interpolación de variables en una cadena de texto. Esto significa 
que puede reemplazar fragmentos de código con sus valores sin tener que 
concatenar cadenas. Se escriben entre comillas triples (```) y pueden 
contener expresiones entre llaves { }.
"""

#Ejemplo:

name = 'Daniel'
age = 29

print(f'Hola, mi nombre es {name} y tengo {age} años.')

#Salida: Hola, mi nombre es Daniel y tengo 29 años.

texto_largo = """
    Lorem Ipsum es simplemente el texto de relleno de las imprentas y archivos de texto. 
    Lorem Ipsum ha sido el texto de relleno estándar de las industrias desde el año 1500, 
    cuando un impresor (N. del T. persona que se dedica a la imprenta) desconocido usó una 
    galería de textos y los mezcló de tal manera que logró hacer un libro de textos especimen. 
    No sólo sobrevivió 500 años, sino que tambien ingresó como texto de relleno en documentos 
    electrónicos, quedando esencialmente igual al original. Fue popularizado en los 60s con la
    creación de las hojas "Letraset", las cuales contenian pasajes de Lorem Ipsum, y más 
    recientemente con software de autoedición, como por ejemplo Aldus PageMaker, el cual 
    incluye versiones de Lorem Ipsum.
"""

print(texto_largo)