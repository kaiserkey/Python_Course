""" import os, time

path = os.getcwd()# Ruta de la carpeta que queremos revisar

def timesOfArchives(path):
    # Obtenemos la lista de archivos y carpetas dentro de la carpeta
    current_archives= os.listdir(path)
    # Obtenemos los tiempos de modificación de los archivos en un diccionario
    return {archive:os.stat(f"{path}/{archive}").st_mtime for archive in current_archives}
    
    # List Comprehension
    # [item: <expr> for <elemento> in <lista>]
    # Donde <expr> es una expresión que se evalúa para cada elemento de la lista <lista>. 
    # El resultado de <expr> se asigna al elemento con nombre <item>.
    

def saveModifiedFiles(current_times):
    # Guardamos los tiempos de modificación de los archivos en un archivo
    with open('previous_times.txt', 'w') as archive:
        for archives, times in current_times.items():
            archive.write(f'{archives},{times}\n')

def countdown(tiempo):
    # Contador regresivo
    for i in range(tiempo, 0, -1):
        print(f"\033[1;33m/===============( {i} )===============/\033[0m")
        time.sleep(1)
        os.system('clear')

def compareChanges(current_times, new_times):
    listOfChanges = []
    # Recorremos los nuevos tiempos de modificación
    for archive, times in new_times.items():
        if archive in current_times:
            # Si el archivo ya existía, revisamos si el tiempo de modificación ha cambiado
            if times != current_times[archive]:
                listOfChanges.append(archive)
                print(f'\033[1;32mEl archivo {archive} ha tenido cambios\033[0m')
                time.sleep(3)
        else:
            # Si el archivo es nuevo, mostramos un mensaje
            print(f'\033[1;32mSe agrego un nuevo archivo: {archive}\033[0m')
            listOfChanges.append(archive)
            time.sleep(3)

saveModifiedFiles(timesOfArchives(path))
current_times = timesOfArchives(path)

# Revisamos la carpeta cada cierto tiempo
while True:
    new_times = timesOfArchives(path)
    compareChanges(current_times, new_times)
    # Actualizamos los tiempos de modificación
    current_times = new_times
    countdown(5)  """


""" from github import Github
import os

myGitHub = Github("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")

repositories = []

# Then play with your Github objects:
for repo in myGitHub.get_user().get_repos():
    repositories.append(repo.full_name)

for index in range(0,len(repositories)):
    print(f"\t\033[1;34m{index+1}. {repositories[index]}\033[0m")

option = 0
selected = ""

while True:
    print()
    option = int(input("\t\033[1;35mSelecciona un repositorio: "))
    print("\033[0m")
    if option > 0 and option <= len(repositories):
        selected = repositories[option-1]
        break
    else:
        print("Invalid option")

# Seleccionar el repositorio para el que se subirán los cambios y la rama
repo = myGitHub.get_repo(selected)
#print(dir(repo))

contents = repo.get_contents("ejercicio99.py", ref="main")
repo.update_file(contents.path, "more tests", "more tests", contents.sha, branch= "main")"""

import os 

os.system('git add .')
os.system('git commit -m "more tests"')
os.system('git push origin main')