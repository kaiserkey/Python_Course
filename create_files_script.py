import os

maxArchives = int(input("¿Cuántos archivos quieres crear? "))

for i in range(maxArchives):
    # Creamos el archivo si no existe
    if(not(os.path.isfile("ejercicio"+str(i+1)+".py"))):
        file =open("ejercicio"+str(i+1)+".py","w")


