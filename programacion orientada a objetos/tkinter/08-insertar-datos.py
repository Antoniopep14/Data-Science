import sqlite3


def insertar():
    # este metodo crea el enlace a la base de datos
    db1 = sqlite3.connect("novelas.db")
    print("estas en la funcion insetar")

    nombre1 = input("Escribe el titulo de la novela")
    autor1 = input("Escribe el autor de la novela")
    year1 = str(input("Digita el año de la novela"))
# ahora habilitamos la conexion con el metodo cursor
    consulta = db1.cursor()
# ahora asignamos la entradas correspodientes a la tabla a una variable
    strConsulta = "insert into tabla(nombre, autor, year)values(" + \
        nombre1+","+autor1+","+year1+")"
    print(strConsulta)
    # ahora usamos el metodo execute para ejecutar una funcion sql
    # despues desabilitamos la conexion
    consulta.close
    # y guardamos los cambios
    db1.commit()
    db1.close()


insertar()
