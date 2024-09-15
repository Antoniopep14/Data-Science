#ahora vamos a ver como realizar operaciones con sqlite
#pero sin necesidad de estar constantemente comprometiendo los cambios
#o tambien cerrando nuestra coneccion

import sqlite3
with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute(
        """
        CREATE TABLE if not exists usuarios
        (id INTEGER primary key, nombre VARCHAR(50));
        """
        )
#el ejecutar en with ya no es necesario ejecutar commit ni close
