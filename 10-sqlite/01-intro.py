import sqlite3
#estamos trabajando sobre la carpeta de curso-py
#primero generamos una conexion con la db usando el metodo connect
con = sqlite3.connect("sqlite/app.db")
#como el archivo no existe, python lo va a crear
#si no cerramos la conexion a la base de datos
#no vamos a poder excribir en ella despues
#ES MUY IMPORTANTE CERRARLA siempre que la abrimos
con.close()


