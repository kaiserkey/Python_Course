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

    # Obtenemos la lista de archivos y carpetas dentro de la carpeta
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

        # Recorremos los nuevos tiempos de modificación
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

    detectar cambios en archivos locales con pygithub en python

    Para detectar cambios en los archivos locales con PyGithub en Python, 
    primero necesitas crear un repositorio en Github. Una vez creado el repositorio, 
    puedes usar el método Repository.get_commits para obtener la lista de los últimos 
    commits realizados.

    Para cada commit, puedes usar el método Commit.get_files para obtener la 
    lista de archivos modificados. Una vez que tengas la lista de archivos, 
    puedes recorrerla para obtener las URLs de los archivos y descargarlos en 
    tu computadora. Luego, puedes usar alguna librería para comparar los archivos 
    descargados con los archivos locales y determinar si hay alguna diferencia.

    Aquí hay un ejemplo de cómo puedes implementar esto en Python:

    import requests
    from github import Github

    # Autenticación en Github
    g = Github("username", "password")

    # Obtenemos el repositorio
    repo = g.get_repo("username/repository")

    # Obtenemos los últimos commits
    commits = repo.get_commits()

    # Recorremos cada commit
    for commit in commits:
        # Obtenemos la lista de archivos modificados
        archivos = commit.get_files()

        # Recorremos cada archivo
        for archivo in archivos:
            # Obtenemos la URL del archivo
            url = archivo.raw_url

            # Descargamos el archivo
            r = requests.get(url)
            data = r.text

            # Aquí puedes usar alguna librería para comparar el archivo descargado con el archivo local y determinar si hay alguna diferencia.








    Automatizar la subida de cambios nuevos a github con python

    Puede automatizar la subida de cambios nuevos a GitHub con Python usando la biblioteca PyGithub. Esta biblioteca le permite conectarse a su cuenta de GitHub, examinar los repositorios, crear nuevos repositorios, crear ramas, crear pulgares, enumerar archivos, y mucho más. Esta biblioteca le permite automatizar la subida de cambios nuevos al repositorio de GitHub mediante el uso de métodos lógicos y loops.

    Ejemplo explicado:

    1. Primero, necesita importar la biblioteca PyGithub en su script de Python.

    2. Luego, debe iniciar sesión en su cuenta de GitHub usando la función de autenticación de PyGithub.

    3. Una vez que haya iniciado sesión, puede utilizar los métodos proporcionados por la biblioteca para enumerar los repositorios existentes en su cuenta.

    4. Luego, debe elegir el repositorio en el que desea subir los cambios nuevos.

    5. Después de seleccionar el repositorio, puede usar el método PyGithub para obtener el árbol de contenido del repositorio. Esto le permitirá ver los archivos existentes en el repositorio.

    6. A continuación, debe crear un bucle para enumerar los archivos existentes en el repositorio.

    7. Por último, dentro del bucle, puede usar el método PyGithub para subir los cambios nuevos al repositorio.

    Ejempĺo practico:

    import github

    # Iniciar sesión en la cuenta de Github usando la autenticación
    g = github.Github("usuario", "contraseña")

    # Obtener la lista de repositorios existentes en la cuenta
    repos = g.get_user().get_repos()

    # Seleccionar el repositorio para el que se subirán los cambios
    repo = g.get_repo("usuario/repo_nombre")

    # Obtener el árbol de contenido del repositorio
    tree = repo.get_git_tree("master", recursive=True).tree

    # Enumerar los archivos existentes en el repositorio
    for archivo in tree:
        # Subir los cambios nuevos al repositorio
        repo.create_git_blob(archivo.path, archivo.type, archivo.data)

    # Finalmente, enviar los cambios al repositorio
    repo.commit("Mensaje de commit")

    Detectar los ultimos cambios en archivos con PyGithub

    Puede detectar los últimos cambios en los archivos usando la biblioteca PyGithub. Esta biblioteca le permite conectarse a su cuenta de GitHub y examinar los repositorios. Esta biblioteca le permite detectar los últimos cambios en los archivos mediante el uso de métodos lógicos y loops.


    Ejemplo explicado:

    1. Primero, necesita importar la biblioteca PyGithub en su script de Python.

    2. Luego, debe iniciar sesión en su cuenta de GitHub usando la función de autenticación de PyGithub.

    3. Una vez que haya iniciado sesión, puede utilizar los métodos proporcionados por la biblioteca para enumerar los repositorios existentes en su cuenta.

    4. Luego, debe elegir el repositorio del que desea detectar los últimos cambios.

    5. Después de seleccionar el repositorio, puede usar el método PyGithub para obtener el árbol de contenido del repositorio. Esto le permitirá ver los archivos existentes en el repositorio.

    6. A continuación, debe crear un bucle para enumerar los archivos existentes en el repositorio.

    7. Dentro del bucle, debe usar el método PyGithub para obtener la fecha de última modificación del archivo.

    8. Por último, debe comparar la fecha de última modificación del archivo con la fecha actual para ver si el archivo se ha modificado recientemente.

    Ejemplo práctico:

    import github
    import datetime

    # Iniciar sesión en la cuenta de Github usando la autenticación
    g = github.Github("usuario", "contraseña")

    # Obtener la lista de repositorios existentes en la cuenta
    repos = g.get_user().get_repos()

    # Seleccionar el repositorio del que desea obtener los últimos cambios
    repo = g.get_repo("usuario/repo_nombre")

    # Obtener el árbol de contenido del repositorio
    tree = repo.get_git_tree("master", recursive=True).tree

    # Enumerar los archivos existentes en el repositorio
    for archivo in tree:
        # Obtener la fecha de última modificación del archivo
        commit = repo.get_commit(archivo.sha)
        fecha_modificacion = commit.commit.committer.date

        # Obtener la fecha actual
        fecha_actual = datetime.datetime.now()

        # Comparar la fecha de última modificación con la fecha actual
        if fecha_modificacion > fecha_actual:
            # Aquí puede escribir el código para realizar cualquier acción,
            # como enviar una notificación por correo electrónico, etc.
            print("El archivo se ha modificado recientemente")
        else:
            print("No hay cambios recientes")
"""


