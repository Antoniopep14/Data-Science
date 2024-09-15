def get_product(**datos):  # se usa **
    print(datos)


# siempre debemos darle nombre al parametro cuando usamos el kwargs
get_product(id="id")  # esto da {'id': 'id'}
# que es un diccionario


def got_product(**datos):
    # si solo queremos usar 1 o 2 de los parametros que metimos usamos los []
    print(datos["id"], datos["name"])


# le podemos dar los parametros que queramos
got_product(id=23,  # se puede poner en una sola linea
            name="iphone",  # si se pone asi igual debe llevar las ,
            desc="Esto es un iphone")
