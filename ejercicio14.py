""" 
    Dado un string, devolver un nuevo string donde la primera y la ultima letra hayan sido intercambiadas.
"""

miFrase = input("Ingrese una frase o texto: ")

print(miFrase[-1] + miFrase[1:-1] + miFrase[0])