#ahora veamos coomo crear una tabla en una db
import sqlite3
con = sqlite3.connect("sqlite/app.db")
#es una buena practica crear el cierre de coneccion enseguida de abrirla
#para poder realizar consultas a una base de datos, necesitamos crear un objeto
#usando el metodo de cursor que va a ser nuestro intermediario
#y seguimos usando el objeto de con para establecer la conexion
cursor = con.cursor()
#ahora si ejecutamos la consulta que queremos realizar con el metodo de execute
#como vamos a pasar una consulta medianamente grande usaremos las """ """
cursor.execute(
    """
    CREATE TABLE if not exists usuarios
    (id INTEGER PRIMARY KEY, nombre VARCHAR(50));
    """
    )
con.commit()
#lo primero indica que creara la tabla usuarios
#lo segundo que creara 2 comlumnas
#para que se ejecute correctamente, despues de execute tenemos que llamar al metodo de commit
#ENTONCES, primero llamamos a cursor, luegos a execute y al final commit
con.close()

#de esta manera hemos creado la tabla en el archivo app.db
