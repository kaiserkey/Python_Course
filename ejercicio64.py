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
    # calculamos el DNI con los numeros introducidos por el usuario
    dni += 10 ** (len[numeros] - i - 1) * numeros[i]

letras = { 0: "T", 1: "R", 2: "W", 3: "A", 
            4: "G", 5: "M", 6: "Y", 7: "F", 
            8: "P", 9: "D", 10: "X", 11: "B", 
            12: "N", 13: "J", 14: "Z", 15: "S", 
            16: "Q", 17: "V", 18: "H", 19: "L", 20: "C", 21: "K", 22: "E" }
# calculamos el resto de la division entre el DNI y 23
    
