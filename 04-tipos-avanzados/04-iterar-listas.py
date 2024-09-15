mascotas = ["pelusa", "pulga", "felipe", "chanchito"]
# las listas son iterables al igual que un str o la funcion range
for mascota in enumerate(mascotas):  # "enumerate" es funcion, tomar nota
    print(mascota)  # arroja la lista en forma de lista
    # (0, 'pelusa')
    # (1, 'pulga')
    # (2, 'felipe')
    # (3, 'chanchito')
    # gracias a la funcion enumerate les asigna un numero del 0 al 3 a cada elemento de la lista
    # y eso es conocido como una tupla
    print(mascota[0])  # esto devuelve los numeros de la tupla 0,1,2,3 (indice)
    print(mascota[1])  # esto da los nombres de las mascotas
# eso quiere ceir que nos esta dando los valores de las columnas 1 y 2

for indice, mascota in enumerate(mascotas):
    # de esta manera le estamos asignando el nombre indice a los numeros
    print(indice, mascota)
    # y mascota a los nombres
    # este deberia ser el codigo final
# 0 pelusa
# 1 pulga
# 2 felipe
# 3 chanchito
