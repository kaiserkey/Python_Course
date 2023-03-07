#1.  Crear un diccionario con 5 elementos de la siguiente forma:

myDictionary =  {
                    'nombre': 'Juan',
                    'edad': 20,
                    'ciudad': 'Madrid',
                    'pais': 'España',
                    'profesión': 'programador'
                }

#2.  Agregar un nuevo elemento al diccionario creado en el ejercicio anterior con la clave 'color_favorito' y el valor 'azul'.

myDictionary.setdefault("color_favorito", "azul")

#3.  Imprimir el valor de la clave 'pais'.

print(myDictionary.get("pais"))

#4.  Recorrer todos los elementos del diccionario creado en el ejercicio 1 imprimiendo cada elemento.

for key, value in myDictionary.items():
    print(f"Clave: {key} -> {value}")

#