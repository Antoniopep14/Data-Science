# para establecer una conexión con una base de datos noSQL
# primero instalar mongo (pip install pymongo)

# importar bibliotecas para hacer establcer la conexión noSQL
from pymongo import MongoClient

client = MongoClient()
db = client.test
# la db test esta instalada por defecto
# insertar datos con el sig comando
# users es la coleccion donde se agregaran
# si esta no existe se creara
db.users.insert_one({'name': 'Cristal P'})
# para crear varios documentos a la vez
db.users.insert_many([{'name': 'Holly'}, {'name': 'Pete'}])
# podemos agregar muchos atributos en cada documento
# incluso cada atributo puede tener un arreglo de subatributos
result = db.users.insert_one(
    {
        "name": "Vella",
        "address": {
            "street": "2 Avenue",
            "zipcode": "10075",
            "building": "1480",
        }
    }
)

# ahora realizaremos una consulta de los elementos en la coleccion con find
print("Insertar y consultar" + '\n')
cursor = db.users.find()
for document in cursor:
    print(document)

#podemos actualizar un documento con
db.users.update_one({"name":"cristal P"}, {"$set":{"name": "Cris P"}})
#ver modificar
print("actualizar" +'\n')
cursor = db.users.find()
for document in cursor:
    print(document)

#para borrar un documento
#si quisieramos borrar multiples documentos a la vez cambiar one por many
result = db.users.delete_one({"name": "Cris P"})
print(result.deleted_count)

#ver borrar
print("borrar" +'\n')
cursor = db.users.find()
for document in cursor:
    print(document)

