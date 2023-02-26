""" 
    La sucesión de Fibonacci es una sucesión infinita que se caracteriza 
    porque cada término es la suma de los dos anteriores. Algunos de sus 
    términos son 1, 1, 2, 3, 5, 8, 13...

    Supongamos que queremos que se nos impriman los 20 primeros términos de 
    esta serie. Por tanto, necesitaremos por un lado los términos de la serie 
    y, por otro, los índices que ocupan.

    Ejercicio. Pensad en cómo podríais resolver este problema en el cual se 
    exige que en algún momento utilicéis el comando break.
"""
fibo_ant = 1 # Término anterior
fibo = 1 # Término actual
idx = 3 # Como ya tenemos los dos primeros términos, empezamos con el índice 3

print(f"El término {fibo_ant} ocupa la posición {1}")
print(f"El término {fibo} ocupa la posición {1}")

while fibo <= 5000000: # Establecemos una cota para que el bucle no sea infinito
    temp = fibo  # Guardamos temporalmente el fibonacci actual 
    fibo = fibo + fibo_ant  # Calculamos el nuevo término de la sucesión
    fibo_ant = temp # Modificamos el valor del término anterior
    
    print(f"El término {fibo} ocupa la posición {idx}")
    
    if idx == 25: # Si llegamos al vigésimo índice, 
        break       # salimos del bucle
    
    idx += 1 # Incrementamos el valor del índice