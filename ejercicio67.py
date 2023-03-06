""" 
    Metodos de diccionarios
"""

# el metodo clear() elimina todos los elementos del diccionario
dicc = { "animal": "perro", "edad": 5, "raza": "pastor aleman" }
print(dicc)
dicc.clear()
print(dicc)

# el metodo copy() devuelve una copia del diccionario
dicc = { "animal": "perro", "edad": 5, "raza": "pastor aleman" }
dicc_copy = dicc.copy()
print(dicc_copy)

# el metodo fromkeys() crea un nuevo diccionario con las claves especificadas y el valor especificado
dicc = dict.fromkeys(["animal", "edad", "raza"], "desconocido")
print(dicc)

# el metodo get() devuelve el valor de la clave especificada
print(dicc.get("animal")) # desconocido
print(dicc.get("color")) # None

# el metodo pop() elimina el elemento con la clave especificada y devuelve su valor
print(dicc) # {'animal': 'desconocido', 'edad': 'desconocido', 'raza': 'desconocido'}
print(dicc.pop("animal")) # desconocido
print(dicc) # {'edad': 'desconocido', 'raza': 'desconocido'}

# el m