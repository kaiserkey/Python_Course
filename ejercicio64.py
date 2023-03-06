""" 
    Vamos a solicitar al usuario 8 numeros enteros del 0 al 9.
    A continuacion, con esos numeros calcularemos la letra correspoondiente
    y la guardaremos en una variable. Finalmente, crearemos un diccionario
    con dos claves, cada una guardara, respectivamete, los numeros y la letra del DNI. 
    Finalmente, mostraremos el diccionario por pantalla.
"""

print("Introduce 8 numeros del 0 al 9 para calcular tu letra del DNI")
numeros = []
for _ in range(8):
    numeros.append(int(input("-> ")))

dni = 0
for i in range(len(numeros)):
    # calculamos el DNI con los numeros introducidos por el usuario y lo guardamos en la variable dni
    dni += 10 ** (len[numeros] - i - 1) * numeros[i]

