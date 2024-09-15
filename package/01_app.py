# para instalar paquetes desde pypi
# -debemos cerrar la carpeta de la barra de navegacion a la izquierda
# -abrir la terminal de vscode o cmd
# - pip install NombreDePaquete
# -para ver los paquetes de pip instalados usaremos el comando: pip list
# -para eliminar un paquete usamos: pip unistall nombredepaquete
# despues nos preguntara Y/n y escribimos Y
# -si queremos instalar alguna version en especifico podemos usar: pip install nombrepaquete==2.18.* donde el * quiere decir la ultima version disponible de la 2.28
# o puede ser 2.* para la ultima version de la 2.x
# -para instalar paquetes que "se parezcan" usaremos: pip install requests~=2.18.1 
# (instalo la 2.18.4) por	que hace los mismo que el *
#Al desinstalar paquetes tenemos que fijarnos si las dependencias de ellos tambien se desinstalan
#sino deberemos hacerlo manualmente con el comando, despues de ver con list cual es la que debemos quitar
#para instlar el paquete de nuevo y que este venga con su dependencia actualizada


import requests

r = requests.get("https://www.google.com.co")
print(r) #<Response [200]>
#para saber que es ese 200 buscamos en google http status codes

#AMBIENTES VIRTUALES
#Cuando nosotros trabajamos con paquetes externos al compartir el codigo
#Las personas que tengan acceso a el podrian no poder usarlo
#debido a la falta de paquetes, para eo sirven los ambientes virtuales
#NUEVAMENTE trabajaremos sobre la terminal de comandos
#primero escribimos python -m venv env
#al dar clic nos va a dar error con request porque no esta instalado en nuestro entorno virtual
#pero antes de solucionarlo vamos a ver el contenido de la carpeta que se creo "env"
#en la subcarpeta "lib" podemos ver todas las dependencias instaladas en el ambiente virtual
# "scripts" nos muestra las versiones de python y pip que estmos usando
#el scrip de activate que viene en la misma carpeta nos sirve para activar el ambiente virtual en el que estamos trabajando
# para hacer eso NUEVAMENTE nos vamos a la terminal integrada y escribimos
# env\Scripts\activate.bat
#CHATGPT
#Si estás usando la terminal integrada de VSCode en Windows y tienes problemas 
#con la activación del entorno virtual usando el archivo activate.bat, 
#podría deberse a la política de ejecución de scripts de PowerShell.
#SE SOLUCIONO EJECUTANDO
#Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
#este codigo se debe ejecutar cada vez que cierras y abres vscode
#.\env\Scripts\Activate
#LISTO

#ahora si tenemos que instalar request de nuevo usando:
#pip install requests

#para desactivar el ambiente virtual usamos el comando
# deactivate


