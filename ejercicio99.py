""" 
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


