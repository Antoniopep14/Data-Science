#ahora obtengamos todos los registros de la db
import sqlite3
with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute("SELECT * from usuarios")
    print(cursor.fetchall())
#[(1, 'Hola Mundo'), (2, 'Chanchito feliz'), (3, 'Chanchito triste')]
#solo tenemos que cambiar el fetchone por all al final
