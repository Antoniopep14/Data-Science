import sqlite3


def insertar():
    db1 = sqlite3.connect("novelas.db")
    print("estas en la funcion insetar")

    nombre1 = input("Escribe el titulo de la novela: ")
    autor1 = input("Escribe el autor de la novela: ")
    year1 = input("Digita el año de la novela: ")
    consulta = db1.cursor()
    strConsulta = "insert into tabla(nombre, autor, year)values(" + \
        nombre1+","+autor1+","+year1+")"
    print(strConsulta)
    consulta.close()
    db1.commit()
    db1.close()

# las consultas tienen por objetivo recuperar datos de la tablas


def consultar(db):
    # creamos el enlace a la base de datos
    print("estas en la funcion consultar")
    # ahpra preparamos la consulta con el sig metodo
    db.row_factory = sqlite3.Row
    # habilitamos la conexion con el metodo cursor
    consulta = db.cursor()
    # ejecutamos la instruccion sql para hacer una consulta
    consulta.execute("SELECT * FROM tabla")
    # ahora guardamos el resultado de la consulta
    filas = consulta.fetchall()
    # ahora creamos una lista vacia y usamos for para agregar los registros
    print("Número de filas encontradas:", len(filas))
    lista = []
    for fila in filas:
        s = {"nombre": fila["nombre"],
             "autor": fila["autor"],
             "year": str(fila["year"])}
        lista.append(s)
# ahora desabilitamos la conexion y cerramos la conecxion
    consulta.close()
    print("Resultados:", lista)
    return lista


# consultar()

# ahora se hace un menu de seleccion para hacer inserciones y consultas automaticamente


def menu():
    db = sqlite3.connect("novelas.db")

    while True:
        opcion = input(
            "\n1. insertar un valor en la tabla\n2. consultar los valores de la tabla\n0. salir\nIngresa la opción deseada: ")

        if opcion == "1":
            insertar()
        elif opcion == "2":
            listanovelas = consultar(db)
            for novela in listanovelas:
                print(novela["nombre"], novela["autor"], novela["year"])
        elif opcion == "0":
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

    db.close()


menu()
