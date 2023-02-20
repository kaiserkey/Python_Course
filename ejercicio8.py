""" 
    El orden de los operadores es el siguiente:
    Primero se evaluan los parentesis
    Segundo se evaluan las potencias
    Tercero se evaluan las multiplicaciones y divisiones, en orden de izquierda a derecha
    Cuarto se evaluan las sumas y restas, en orden de izquierda a derecha
"""

#Ejemplo
print(6+2*8/4-2**3) #2.0

print((6+2)*(8/(4-2))**3) # 512.0

print((6+2)*8/(4-2)**3) # 8.0