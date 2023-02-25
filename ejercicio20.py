""" 
    El método "in" en Python se utiliza para verificar si un valor está presente en 
    una secuencia (lista, tupla, diccionario, etc.). Devuelve un valor booleano 
    (True o False) dependiendo de si el elemento específico se encuentra en la secuencia.
"""

texto = "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua."

if " " in texto:
    print("EL Texto Contine " , texto.count(" ") , " espacios")