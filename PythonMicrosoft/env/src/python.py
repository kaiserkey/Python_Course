""" 

-pip venv env se usa para crear un entorno virtual

-./env/Scripts/activate se usa para activar el entorno virtual

-./env/Scripts/deactivate se usa para desactivar el entorno virtual

-pip freeze se usa para ver los paquetes instalados en el entorno virtual

-pip freeze > requirements.txt se usa para guardar los paquetes instalados en el entorno virtual

-pip install -r requirements.txt se usa para instalar los paquetes guardados en el entorno virtual

-pip install python-dateutil==1.4 se usa para instalar una versión específica de un paquete en el entorno virtual

-pip install --upgrade python-dateutil se usa para actualizar un paquete en el entorno virtual

-pip install python-dateutil==randomwords se usa para averiguar qué versiones están disponibles

-pip uninstall python-dateutil se usa para desinstalar un paquete en el entorno virtual

-pip freeze python-dateutil se usa para ver si un paquete está instalado en el entorno virtual

-versionamiento semántico (semver) se usa para especificar versiones de paquetes en el entorno virtual (MAJOR.MINOR.PATCH)

-MAJOR: cambios que no son compatibles con versiones anteriores

-MINOR: cambios que son compatibles con versiones anteriores

-PATCH: cambios que son compatibles con versiones anteriores y que corrigen errores

-pip install "python-dateutil==2.7.*" --upgrade se usa para actualizar un paquete en el entorno virtual a la última versión de la serie 2.7 (2.7.0, 2.7.1, 2.7.2, etc.) 

-pip uninstall -r requirements.txt -y se usa para desinstalar todos los paquetes de un entorno virtual a la vez (el -y es para que no pregunte si queremos desinstalar cada paquete)


"""