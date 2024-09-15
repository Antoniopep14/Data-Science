# ahora aprenderemos a trabajar con archivos separados por , o CSV
import csv
import os
# # ESCRIBIR
# with open("archivos/archivo.csv", "w") as archivo:
#     # ahora tenemos que crear un objeto apartir de csv
#     # con el archivo que le queremos asignar al metodo
#     write = csv.writer(archivo)
#     # con write nosotros vamos a poder acceder al archivo
#     # ahora le pasamos un metodo a write con un par de cabeceras y el texto o contenido
#     write.writerow(["twit_id", "user_id", "text"])
#     # writerow escribe una fila en un archivo csv
#     # ahora le agregamos los identificadores
#     writer.writerow(["1000", "1", "este es un twit"])
#     writer.writerow(["1001", "2", "otro twit"])
# # al ejecutar creo el archivo csv con los identificaodores que le dimos

# # Ahora veamos como LEER archivos csv
# # recordar que si no le pasamos ningun modo, entra el de lectura por default
# with open("archivos/archivo.csv") as archivo:
#     # ahora creamos un objeto con .reader
#     read = csv.reader(archivo)
#     # print(read)#esto nos da un objeto iterable
#     # #<_csv.reader object at 0x0000019623A76F20>
#     # si queremos ver los datos, podemos convertirlo a una lista
#     # print(list(reader))
#     # o podemos iterar el archivo
#     for linea in reader:
#         print(linea)
# recordar que si queremos ejecutar los 2 metodos para extraer datos al mismo tiempo tendriamos que usar:
#     archivo.seek(0)

# ahora veamos como extraer y modificar una linea dentro del archivo csv
# ACTUALIZAR CSV
# tenemos que llamar a a funcion de open y como no podemos abrir y editar un archivo al mismo tiempo
# tenemos que crear un archivo temporal donde vamos a trabajar
with open("archivos/archivo.csv") as r, open("archivos/archivo_temp.csv", "w",  newline='') as w:
### el newline lo agregue para qeu al ejecutar el codigo, no me separe el contenido por lineas cada vez que lo hago
    # ahora creamos 2 objetos, uno para el metodo de reader y otro para writer
    reader = csv.reader(r)  # le pasamos la referencia de reader r
    writer = csv.writer(w)  # le pasamos la referencia de writer w temporal
    # ahora iteramos el archivo linea por linea
    # supongamos que quiero cambiar el id de tuit
    #para lo cual vamos a leer y pasar linea por linea de r a w
    #pero al encontrar la linea que queremos cambiar le va a pasar una linea modificada
    for linea in reader:
#es importante tomar nota de que todos los datos separados por , van a ser transformados en un str
        if len(linea) > 0 and linea[0] == "1000":
###al querer ejecutar por segunda vez daba error por lo que agregue
### if len(linea) > 0 and
### para que verificar primero si existe la linea y no un espacion en blanco
            writer.writerow([1000, 1, "texto modificado 2"])
        else:
            # si no tiene 1000 la linea, dejala como esta
            writer.writerow(linea)
# ahora que ya modificamos el archivo, tenemos que eliminar el archivo csv y reemplazarlo por el temp ya modificado
# para lo cual hacemos import os
# que nos va a permitir eliminar y renombrar archivos
os.remove("archivos/archivo.csv")
os.rename("archivos/archivo_temp.csv", "archivos/archivo.csv")

# al ejecutar habremos modificado la linea del archivo csv
