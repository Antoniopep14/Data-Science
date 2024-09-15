# Variables de entorno
#cuando compartimos codigo que tenga contraseñas en nuestro codigo
#quedamos expuestos a que nos las roben, para ello debemos ocultarlas, pero al mismo tiempo permitir el uso de ellas
#SENGRID_API_KEY = "contraseñaquequeremosocultar"
#primero creamos el archivo env y copiamos la variable de arriba, que seria el pass que queremos ocultar
import os

apikey = os.environ.get("SENDGRID_API_KEY")
print(apikey)
#ahora creamos un ambiente virtual e instalamos el paquete sendgrid
#pipenv install sendgrid
#como nos muestra el valor de none, debemos de activar la shell
#usando: pipenv shell
#nos debe mostrar este mensaje: Launching subshell in virtual environment...
#ahora ejecutamos con: python 01-env.py
# y ya nos muestra la contraseña que queriamos ocultar/ver

#para cambiar el entorno vitual tenemos que ver la ruta usando:
#pipenv --venv
#y pegarla en la interfaz de interpretes
#o acutalizar la lista de interpretes y seleccionar el nuestro

#despues de todo creamos un archivo llamado .gitignore
#de esta manera cuando hagamos cambios en el archivo env, esos no se va a subir al repositorio
#pero las personas que quieran usar el repositorio van a tener la responsabilida de poblar el archivo env

