""" 
    Realizar un bucle for que imprima una cadena al revez
"""

texto = "lorem ipsum dolor sit amet"
invertido = ""

for c in texto:
    invertido = c + invertido
    
print(invertido)