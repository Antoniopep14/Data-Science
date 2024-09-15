# una tupla es lo mismo que una lista pero no se puden modificar, ni quitar ni agregar elementos
# usualmente se usan cuando no queremos modificar los elementos de una lista accidentalmente
# aunque si se pueden crear nuevas tuplas a partir de una ya existente
# estas van con () en lugar de []
numeros = (1, 2, 3) + (4, 5, 6)
print(numeros)

# Si queremos transformar una lista en tupla, usaremos el metodo "tuple()"
# punto = [1, 2]

punto = tuple([1, 2])
print(punto)
# con las tuplas podemos usar los mismos metodos que las listas
# a escepcion de los que la modifican como apend o pop
# pero si podemos acceder a los elementos de la tupla
menosnumeros = numeros[:2]  # y esto crearia una nueva tupla
print(menosnumeros)
# tambien podemos desempaquetar las tuplas
primeroy, seugundoy, *otrosy = numeros
# 1 2 [3, 4, 5, 6] y esto ya nos devuelve una lista
print(primeroy, seugundoy, otrosy)

# tambien podemos iterar las tuplas
for n in numeros:
    print(n)

# numeros[0] = 5 #esto es imposible porque no podemos modificar las tuplas
# si queremos modificar la tupla, tenemos que extraer una lista de ella
# y despues modificamos esa lista extraida
listaNumeros = list(numeros)
listaNumeros[0] = "pepe feliz"
print(listaNumeros)
