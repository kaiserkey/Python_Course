""" 
    Los diccionarios en Python son una estructura de datos que se utiliza para 
    almacenar y organizar información de manera eficiente. Están compuestos de 
    pares de clave-valor, donde cada clave se asocia con un valor que se puede 
    usar para recuperar la información. Esto significa que los diccionarios 
    permiten acceder a los datos de forma rápida y eficiente sin necesidad de 
    recorrer la lista completa de elementos. Esta es una de las principales 
    razones por las que los diccionarios son tan útiles para el procesamiento 
    de datos en Python.
"""

myDictionary = { "nombre": "Juan", "apellido": "Perez", "edad": 25, "cursos": ["Python", "Django", "JavaScript"] }

print(myDictionary)
print(myDictionary["cursos"])

# Se puede convertir un iterable en un diccionario con la funcion dict()
# Debe tener un formato de clave-valor
dict = dict([("nombre", "Juan"), ("apellido", "Perez"), ("edad", 25), ("cursos", ["Python", "Django", "JavaScript"])])

print(dict)

dict2 = dict(["x", 3], ["y", 4], ["z", 5], 3)