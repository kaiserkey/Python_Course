""" 
    Metodos para trabajar con strings
"""

texto = " HOLA Mundo "

print(texto.lower()) # Convierte el string a minusculas
print(texto.upper()) # Convierte el string a mayusculas
print(texto.capitalize()) # Convierte el primer caracter del string a mayuscula
print(texto.title()) # Convierte el primer caracter de cada palabra del string a mayuscula
print(texto.swapcase()) # Convierte las mayusculas a minusculas y viceversa
print(texto.count("o")) # Cuenta la cantidad de veces que aparece un caracter en el string
print(texto.count("O", 0, 4)) # Cuenta la cantidad de veces que aparece un caracter en el string entre un rango de indices
print(texto.replace("o", "a")) # Reemplaza un caracter por otro
print(texto.find("o")) # Busca un caracter en el string y devuelve la posicion del primer caracter encontrado
print(texto.find("o", 0, 4)) # Busca un caracter en el string entre un rango de indices y devuelve la posicion del primer caracter encontrado
print(texto.split(" ")) # Divide el string en una lista de strings
print(texto.strip()) # Elimina los espacios en blanco al inicio y al final del string
print(texto.lstrip()) # Elimina los espacios en blanco al inicio del string
print(texto.rstrip()) # Elimina los espacios en blanco al final del string
print(texto.startswith("H")) # Verifica si el string comienza con el caracter especificado
print(texto.endswith("o")) # Verifica si el string termina con el caracter especificado
print(texto.isalpha()) # Verifica si el string contiene solo caracteres alfabeticos
print(texto.isalnum()) # Verifica si el string contiene solo caracteres alfanumericos
print(texto.isdigit()) # Verifica si el string contiene solo caracteres numericos
print(texto.islower()) # Verifica si el string contiene solo caracteres en minusculas
print(texto.isupper()) # Verifica si el string contiene solo caracteres en mayusculas
print(texto.istitle()) # Verifica si el string contiene solo caracteres en mayusculas y minusculas
print(texto.isnumeric()) # Verifica si el string contiene solo caracteres numericos
print(texto.isdecimal()) # Verifica si el string contiene solo caracteres numericos
print(texto.isprintable()) # Verifica si el string contiene solo caracteres imprimibles
print(texto.isspace()) # Verifica si el string contiene solo caracteres de espacio
print(texto.index("o")) # Busca un caracter en el string y devuelve la posicion del primer caracter encontrado
#print(texto.index("O", 0, 4)) # Busca un caracter en el string entre un rango de indices y devuelve la posicion del primer caracter encontrado
print(texto.rfind("o")) # Busca un caracter en el string y devuelve la posicion del ultimo caracter encontrado
print(texto.rfind("o", 0, 4)) # Busca un caracter en el string entre un rango de indices y devuelve la posicion del ultimo caracter encontrado
print(texto.rindex("o")) # Busca un caracter en el string y devuelve la posicion del ultimo caracter encontrado
#print(texto.rindex("o", 0, 4)) # Busca un caracter en el string entre un rango de indices y devuelve la posicion del ultimo caracter encontrado
print(texto.join(", Join")) # Une el string con cada caracter de la cadena especificada
print(texto.center(50, "-")) # Centra el string en un campo de caracteres especificado
print(texto.ljust(50, "-")) # Alinea el string a la izquierda en un campo de caracteres especificado
print(texto.rjust(50, "-")) # Alinea el string a la derecha en un campo de caracteres especificado
print(texto.zfill(50)) # Rellena el string con ceros a la izquierda hasta completar el campo de caracteres especificado
print(texto.partition("u")) # Divide el string en una tupla de 3 elementos, el primer elemento es el string antes del caracter especificado, el segundo elemento es el caracter especificado y el tercer elemento es el string despues del caracter especificado
print(len(texto))