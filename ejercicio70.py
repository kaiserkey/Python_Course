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

for key, value in myDictionary.items():
    print(f"Clave: {key}")
    for value in value.items():
        print(f"Clave: {value[0]} -> {value[1]}")