""" from github import Github
g = Github("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")

# Then play with your Github objects:
for repo in g.get_user().get_repos():
    print(repo.name) """
    
import os, time

path = os.getcwd()# Ruta de la carpeta que queremos revisar

def timesOfArchives(path):
    # Obtenemos la lista de archivos y carpetas dentro de la carpeta
    current_archives= os.listdir(path)
    # Obtenemos los tiempos de modificación de los archivos en un diccionario
    return {archive:os.stat(f"{path}/{archive}").st_mtime for archive in current_archives}
    """ 
        List Comprehension
        [item: <expr> for <elemento> in <lista>]

        Donde <expr> es una expresión que se evalúa para cada elemento de la lista <lista>. 
        El resultado de <expr> se asigna al elemento con nombre <item>.
    """
current_times = timesOfArchives(path)

# Guardamos los tiempos de modificación de los archivos en un archivo
with open('previous_times.txt', 'w') as archive:
    for archives, times in current_times.items():
        archive.write(f'{archives},{times}\n')


""" # Revisamos la carpeta cada cierto tiempo
while True:
    current_archives= os.listdir(path)
    current_times = {archive:os.stat(f"{path}/{archive}").st_mtime for archive in current_archives}
    time.sleep(59) """
    
    
"""
# Recorremos los nuevos tiempos de modificación
for archive, tiempo in current_times.items():
    if archive in current_times:
        # Si el archivo ya existía, revisamos si el tiempo de modificación ha cambiado
        if tiempo != current_times[archive]:
            print(f'El archivo {archive} ha cambiado desde la última revisión')
    else:
        # Si el archivo es nuevo, mostramos un mensaje
        print(f'Se ha encontrado un nuevo archivo: {archive}') """

