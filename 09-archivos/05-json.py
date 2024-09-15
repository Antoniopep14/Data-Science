# El formato json se utiliza cuando nosotros vamos a buscar los datos a una api
# o incluso podria ser una base de datos no relacional como mongodb
# y esto nos va a devolver los datos en un formato json
import json
from pathlib import Path

# # ESCRIBIR json
# productos = [
#     {"id": 1, "name": "surfboard"},
#     {"id": 2, "name": "Bicicleta"},
#     {"id": 3, "name": "skate"}
# ]
# # ahora tenemos que transformar nuestro diccionario y convertirlo en un archivo json
# data = json.dumps(productos)
#dumps  se utiliza para convertir objetos de Python 
# (como diccionarios, listas, cadenas, números, booleanos, etc.) 
# en una cadena de formato JSON. La sigla "dumps" significa "dump string" (volcar a cadena).

# # print(data)# da [{"id": 1, "name": "surfboard"}, {"id": 2, "name": "Bicicleta"}, {"id": 3, "name": "skate"}]
# # se ve igual al listado y diccionarios
# Path("archivos/productos.json").write_text(data)
# # al ejecutar, nos ha creado el archivo json
# #El tipo de dato que nos devulve es el que devuelven la gran mayoria de las apis
# #sobre todo si son rest, y son identicos a los diccionarios en python

# LEER json
# en el parentesis de read_text va la codificacion
data = Path("archivos/productos.json").read_text(encoding="utf-8")
# la argumentacion la podemos hacer poniendo un argumento nombrado uft-8
productos = json.loads(data)
# Ahora ya tenemos un listado de diccionario, que se ve igual que json
print(productos)
# [{'id': 1, 'name': 'surfboard'}, {'id': 2, 'name': 'Bicicleta'}, {'id': 3, 'name': 'skate'}]

# MODIFICAR json
#usamos lo mismo de leer json
# supongamos que queremos cambiar el nombre del primer elemento de nuestro listado
productos[0]["name"] = "chanchito feliz"
# para pasarle el listado de productos, primero tenemos que transformarlo a un archivo json
Path("archivos/productos.json").write_text(json.dumps(productos), encoding="utf-8")
#de nuevo ponemos la codificacion  para evitar el warning
# al ejecutar cambiamos el nombre del primer elemento en el archivo json
# JSON viene de JavaScript Object Notation
# y esta es la forma de como se transmiten los datos en internet
