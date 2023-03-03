""" 

    detectar cambios en archivos de una carpeta con python

    Para detectar cambios en los archivos de una carpeta con Python, 
    puedes usar el módulo os.walk. Esta función recorrerá toda la carpeta 
    y sus subcarpetas y devolverá la lista de todos los archivos y 
    carpetas que están dentro.

    Puedes entonces recorrer la lista de archivos y comparar los tiempos 
    de modificación de cada archivo con los tiempos de modificación anteriores. 
    Si hay algún cambio en los tiempos de modificación, entonces sabrás que algo 
    cambió en el archivo desde la última vez que se revisó.

    Aquí hay un ejemplo de cómo puedes implementar esto en Python:

    import os

    # Ruta de la carpeta que queremos revisar
    ruta = '/home/usuario/carpeta/'

    # Obtenemos la lista de archivos y carpetas dentro de la carpeta.
    
    archivos_actuales = os.listdir(ruta)

    # Obtenemos los tiempos de modificación de los archivos
    tiempos_actuales = {archivo:os.stat(ruta+archivo).st_mtime for archivo in archivos_actuales}

    # Guardamos los tiempos de modificación de los archivos en un archivo
    with open('tiempos_anteriores.txt', 'w') as archivo:
        for archivo, tiempo in tiempos_actuales.items():
            archivo.write('{},{}\n'.format(archivo, tiempo))

    # Revisamos la carpeta cada cierto tiempo
    while True:
        archivos_nuevos = os.listdir(ruta)
        tiempos_nuevos = {archivo:os.stat(ruta+archivo).st_mtime for archivo in archivos_nuevos}

        # Recorremos los nuevos tiempos de modificación..
        for archivo, tiempo in tiempos_nuevos.items():
            if archivo in tiempos_actuales:
                # Si el archivo ya existía, revisamos si el tiempo de modificación ha cambiado
                if tiempo != tiempos_actuales[archivo]:
                    print('El archivo {} ha cambiado desde la última revisión'.format(archivo))
            else:
                # Si el archivo es nuevo, mostramos un mensaje
                print('Se ha encontrado un nuevo archivo: {}'.format(archivo))

        # Actualizamos los tiempos de modificación
        tiempos_actuales = tiempos_nuevos

        # Esperamos antes de revisar nuevamente
        time.sleep(60)
"""


