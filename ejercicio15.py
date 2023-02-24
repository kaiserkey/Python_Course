""" 
    Dado un string, vamos a pedirle al usuario que introduzca una palabra perteneciente a dicho string
    y vamos a obtener el substring sin la palabra que introdujo el usuario
"""

texto = input("Ingrese una un texto: ")
print("Su texto es: " + texto)

palabra = input("Ingrese una palabra perteneciente al texto anterior: ")

if(texto.find(palabra)>=0):
    print("La palabra \"" + palabra + "\" se encuentra en el texto")
    print("El texto sin la palabra " + palabra + " es: " + texto.replace(palabra, "").strip())

