#ahora aprenderemos a insertar datos usando sqlite
import sqlite3
with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute(
        "insert into usuarios values(?, ?)",
        (1, "Hola Mundo"),
    )
#primero pasamos el insert con el ? acorde a los registros
#y despues los registros para evitar una SQL injection
#sql injection es una forma en la cual los hackers pueden acceder a toda tu db
#nunca debemos usar un str formateado para pasar los valores a un db en sql
#podemos usar un ORM que es una biblioteca para evitar eso
# ya sea para insertar, eliminar o lo que sea

#al ejecutar hemos agregado los registros a la db
