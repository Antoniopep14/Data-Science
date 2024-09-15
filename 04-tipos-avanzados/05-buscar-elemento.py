mascotas = ["pelusa", "jacobo", "pulga",
            "wolfgang", "jacobo", "felipe", "chanchito"]
# ahora veremos el metodo "index"
# arroja el indice 2 que es donde se encuentra nuestro elemento
print(mascotas.index("pulga"))

if "wolfgang" in mascotas:  # se usa el if para que no arroje error en caso de no encontrarse el elemento
    print(mascotas.index("wolfgang"))  # arroja el indice 3

# para un dato repetido como "jacobo" primero tenemos que contar cuantos tenemos
# si tratamos de hacer lo mismo de arriba solo nos va a arrojar el indice del primer "jacobo"
# para eso vamos a usar el metodo .count
# da 2, lo que indica que tenemos ese elemento duplicado
print(mascotas.count("jacobo"))
# una vez que sabemos que un elemento de la lista se esta repitiendo, tenemos que eliminar 1
# de preferencia siempre tiene que ser el primero
