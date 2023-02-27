""" 
    1. if not in: Esta instrucción se usa para determinar si un elemento 
    no se encuentra en una secuencia. 

    2. if is: Esta instrucción se usa para verificar si dos variables se 
    refieren al mismo objeto. 

"""

#Ejemplo 1:

my_list = [1,2,3,4]

if 5 not in my_list:
    print("5 no está en la lista")


#Ejemplo 2:

a = [1,2,3]
b = a

if a is b:
    print("a y b se refieren al mismo objeto")

