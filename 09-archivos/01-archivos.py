from pathlib import Path
from time import ctime  # para ver una fecha mas legible
# como este archivo no existia, lo creamos y pegamos lo que copiamos de internet
#lo importante es que el archivo se encuentre separado por lineas
#por que vamos a ver como trabajar con archivos separados por lineas
archivo = Path("archivos/archivo-prueba.txt")
#dentro de los metodos que podemos usar en archivo tenemos:
# archivo.exists() Este metodo se usa para ver si el archivo existe
# archivo.rename() este para renombrarlo
# archivo.unlink() este para eliminarlo
# print(archivo.stat())#va a mostrar, entre otras cosas el tamaño que ocupa en disco, fecha de acceso, de modificacion y creacion
# ya que conocemos el nombre de cada uno vamos a acceder a ellos
#ahora vamos a imprimir todas esas metadatas
# para ver la fecha de acceso a ese archivo
# print("acceso", archivo.stat().st_atime)
# acceso 1698785486.0490234
# ese numero es un timestamp: es la fecha que tiene el archivo con respecto al 1ro de enero de 1970
#ahora importamos ctime para ver la fecha de una forma mas comprensible
print("acceso", ctime(archivo.stat().st_atime))  # modificado con ctime
# esto es una fecha unix
# ya modificado arroja acceso Tue Nov 28 15:25:17 2023
print("creación", ctime(archivo.stat().st_ctime)) #creación Wed Nov 22 00:10:04 2023, cambio de pc
print("modificación", ctime(archivo.stat().st_mtime)) #modificación Tue Oct 31 15:15:08 2023

#Gracias a gpt pude aprender a crear directorios
import os
# Directorio donde se almacenará la base de datos
db_directory = "sqlite"

# Crear el directorio si no existe
if not os.path.exists(db_directory):
    os.makedirs(db_directory)
