from pathlib import Path
archivo = Path("archivos/archivo-prueba.txt")
# texto = archivo.read_text()#va a leer el texto que le indiquemos y mostrarlo como un unico str
# print(texto)
# para gestionarlo de una mejor manera, tenemos que dividirlo en varios strings
# y agruparlos en una lista con el metodo split
texto = archivo.read_text("utf-8").split("\n")
# lo va a separar por cada salto de linea
# print(texto)
##para corregir el warning de archivo.read_text() agregamos una codificacion
# utf-8 es la codificacion con la que estariamos trabajando
# usamos esa por que manejamos ingles y español, ademas de ser la mas extendida acualmente
# de tal manera que nos va a reconocer acentos, ñ, etc

# ahora para modificar el texto, ya podemos trabajarlo directamente con los metodos de lista
texto.insert(0, "Hola mundo!")
# ahora tenemos que indicarle que lo queremos escribir
#pero no podemos pasarle (texto) directamente, porque eso es un listado
# tenemos que pasarle un str
#entonces creamos un str que va a ser un salto de linea y le vamos a agregar el texto
#mas la codificacion con la que queremos guardar el archivo
archivo.write_text("\n".join(texto), "utf-8")

# al ejecutar el codigo e ir al archivo de prueba vemos que agrego el texto hola mundo
# a la primera linea, si lo ejecutamos vuelve a hacer lo mismo una y otra vez
# cuando usamos el metodo read y write estamos extrayendo y modificando el archivo completo
#por lo que al ejecutar write podemos cambiar todo el contenido
#asi que si no queremos eso tenemos que asegurarnos de separar el contenido por salto de linea
#para trabajar en cada una de estas lineas de manera independiente
#y luego volver a escribir sobre ese mismo archivo el str modificado
#si ejecutaramos por ejemplo:
    #archivo.write_text("hola mundo", "utf-8")
    #borrariamos todo y solo quedaria hola mundo
# y esta es la forma mas facil de trabajar con la lectura y escritura de un archivo de un par de megas
# para un archivo con miles o millones de lineas, lo mejor es trabajar con bases de datos
#y no guardar toda la informacion en el mismo archivo
