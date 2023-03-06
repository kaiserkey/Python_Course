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

# el metodo update() actualiza el diccionario con los elementos del diccionario especificado 
# o con los pares clave-valor especificados. Si una clave ya existe, se actualiza su valor. 
# Si no existe, se crea una nueva clave con el valor especificado y se agrega al diccionario.
# Si se especifica un diccionario, se actualizan las claves del diccionario actual con los valores del diccionario especificado.


dicc1 = { "animal": "perro", "edad": 5, "raza": "pastor aleman" }
dicc2 = { "animal": "gato", "edad": 3, "raza": "persa", "color": "negro" }

dicc1.update(dicc2)
print(dicc1)

# el metodo setdefault() devuelve el valor de la clave especificada. Si la clave no existe, inserta la clave con el valor especificado.

dicc1.setdefault("peso", 10)
print(dicc1)