#ahpra aprenderemos a hacer consultas, en especifico a traer un registro
import sqlite3
with sqlite3.connect("sqlite/app.db") as con:
    cursor = con.cursor()
    cursor.execute("SELECT * from usuarios")
    print(cursor.fetchone()) #(1, 'Hola Mundo')

#hay que tomar nota sobre que no fue necesario agregar una variable al metodo de execute
#para despues hacer print con ella ya que derechamente la info queda almacenada en cursor
#como se menciono al inicio solo obtenemos un registro, y simepre va a ser el primero
