#6.  Crear un diccionario con 3 elementos de la siguiente forma:
myDictionary =  {
                    'equipo1': {
                                    'nombre': 'Real Madrid',
                                    'ciudad': 'Madrid'
                                },
                    'equipo2': {
                                    'nombre': 'Barcelona',
                                    'ciudad': 'Barcelona'
                                },
                    'equipo3': {
                                    'nombre': 'Valencia',
                                    'ciudad': 'Valencia'
                                }
                }

#7.  Recorrer todos los elementos del diccionario creado en el ejercicio 6 imprimiendo cada elemento.

for key, items in myDictionary.items():
    print(f"Clave: {key}", end=" -> ")
    for items, value in items.items():
        print(f"Clave: {items} -> {value}")

# 8.  Agregar un nuevo elemento al diccionario creado en el ejercicio 6 con la clave 'equipo4' y los valores 'nombre' y 'ciudad' de tu equipo de fútbol favorito.

myDictionary.setdefault("equipo4", { "nombre": "Manchester United", "ciudad": "Manchester" })

# 9.  Imprimir el valor de la clave 'nombre' del equipo2.

print(myDictionary.get("equipo2").get("nombre"))

# 10.  Eliminar el elemento con la clave 'equipo3' del diccionario.

myDictionary.pop("equipo3")