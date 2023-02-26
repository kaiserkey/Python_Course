""" 
    Break: El break es una instrucción para salir de un bucle. Se utiliza para interrumpir la 
    ejecución de un bucle cuando se cumple una condición. Su sintaxis es:

    for elemento in secuencia:
        --Haz algo con elemento
        if condición:
            break

    Continue: El continue es una instrucción para saltar a la siguiente iteración de un bucle. 
    Se utiliza para omitir la ejecución de una sentencia cuando se cumple una condición. 
    Su sintaxis es:

    for elemento in secuencia:
        --Haz algo con elemento
        if condición:
            continue

"""

# Ejemplo de break y continue

repeat = int(input("¿En que numero quieres que pare el bucle?: "))

for i in range(0, 100):
    if i == repeat:
        break
    
    print(i+1)
else: 
    print("El bucle ha llegado a su maximo valor")
    

number = int(input("¿Que numero quieres saltarte en el bucle?: "))

for i in range(1, 10):
    if i == number:
        print("Salteado")
        continue
    
    print(i)
else: 
    print("El bucle ha llegado a su maximo valor")