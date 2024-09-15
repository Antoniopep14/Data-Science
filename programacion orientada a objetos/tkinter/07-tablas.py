# TODO LO DE LAS TABLAS DESDE AQUI ESTA MAL
# ES IMPORTANTE SABER QUE PUEDO HACER ESTO, PERO CON AYUDA DE GPT
# POR QUE EL CODIGO DE CAPACITATE ES INCORRECTO

# con python podemos crear tablas, insertar registros y consultar regitros
# se importa sqlite3 para poder trabajr con bases de datos
import sqlite3
# creamos una variable con el metodo connect para llamar a la base de datos
conexion = sqlite3.connect("novelas.db")
# ahora llamamos al metodo cursor para habilitar la conexion
consulta = conexion.cursor()
tabla = "CREATE TABLE tabla (id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,"\
    "nombre VARCHAR (30) NOT NULL,"\
        "autor VARCHAR(40) NOT NULL,"\
        "year INTEGER (9) NOT NULL);"

print(tabla)

if (consulta.execute(tabla)):
    print("la tabla fue creada")

else:
    print("la tabla no fue creada")

consulta.close()
conexion.commit()
conexion.close()

# Al ejecutar crea un archivo de base de datos dentro de la carpeta curso.py,
