""" 
    Tenemos un diccionario con 5 claves: Math, English, History, Geography, Biology. Cada clave
    contiene una lista con 3 notas. EL usuario debe introducir cada nota por teclado y luego para cada clave
    se debe mostrar la media de las notas. 
"""

courses = { "Math": [], "English": [], "History": [], "Geography": [], "Biology": [] }

for key in courses:
    for i in key:
        grade = float(input("Ingresa la nota de " + key + ": "))