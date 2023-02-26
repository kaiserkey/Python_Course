""" 
    Do-While: El bucle do-while es una estructura de control de iteración utilizada 
    para asegurar que una sentencia se ejecute al menos una vez. Su sintaxis es:

    do:
    --Haz algo
    while condición
    
    El ciclo do-while es similar al ciclo while, solo que se ejecuta al menos una vez.
    
    Python no tiene una funcionalidad específica para crear un bucle do while cómo 
    otros lenguajes. Pero es posible emular un bucle do while en Python.
"""

#Ejemplo:

palabra_secreta = "python"
counter = 0

while True:
    palabra = input("Ingresa la palabra secreta: ").lower()
    counter = counter + 1
    if palabra == palabra_secreta:
        break
    if palabra != palabra_secreta and counter > 3: 
        break
    
""" 
    El código se ejecutará al menos una vez, preguntando a 
    la persona una palabra.

    Está garantizado que al menos se efectuará una vez True, 
    de otra forma se crearía un bucle infinito.

    Si la persona escribe la clave correctamente, el bucle se 
    habrá terminado.

    De otra manera, si  la persona escribe la clave secreta de forma 
    incorrecta más de tres veces, el bucle se terminará.

    El estado break nos permite controlar el flujo de ejecución del 
    bucle while para no acabar en un bucle infinito.

    break terminará la ejecución del bucle.

    Es así cómo creamos un efecto similar al bucle do while en Python.
"""