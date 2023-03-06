""" 
    Podemos seguir usando un bucle for para recorrer un diccionario, pero en este caso
    no necesitamos usar la funcion range() para obtener los indices de los elementos
"""

dicc = { "animal": "perro", "edad": 5, "raza": "pastor aleman" }

for key in dicc:
    print(key, ":", dicc[key])

# Podemos usar la funcion items() para obtener los pares clave-valor
print( dicc.items() )
