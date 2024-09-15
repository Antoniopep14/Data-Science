# OPERADOR DE DESEMPAQUETAMIENTO

lista = (1, 2, 3, 4)
print(lista)  # [1, 2, 3, 4]
print(*lista)  # 1 2 3 4 #tambien aplica para [tuplas]

# def n(n1, n2, n3)
# podriamos usar ese operador de desempaquetamiento para agregar los parametros a la funcion desde una lista
lista2 = (4, 5, 6)
# tambien podemos combinar listas o tuplas usando este operador
sin_desem = (lista, lista2, 7, 8)
combinada = (*lista, *lista2, 7, 8)  # y agregarle elementos extra
print(sin_desem)  # ((1, 2, 3, 4), (5, 6), 7, 8)
print(combinada)  # (1, 2, 3, 4, 5, 6, 7, 8)

# esta operacion tambien se puede usar en los diccionarios
# la dif es que se usan 2 ** en lugar de 1 *
punto1 = {"x": 19}
punto2 = {"y": 15}

# siempre se usa el mismo operador de que los estamos extrayendo (). [], {}
# la asignacion de puntos va de derecha a izq
nuevoPunto = {**punto1, **punto2, "z": 23}
# por lo que si en el punto 1 hubiera un valor y=a
# no se tomaria en cuenta ya que ya tenemos un valor y=15 en punto2
print(nuevoPunto)  # {'x': 19, 'y': 15, 'z': 23}
