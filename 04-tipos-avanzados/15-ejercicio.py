# este lo hacemos para poder usar el pprint y ver los diccionarios de forma mas elegante
from pprint import pprint
# lo que hace es ponerlos uno debado de otro

string1 = "aneel esta afuera"


def no_space_lista(texto):
    # podemos usar el return directamente porque estamos obteniendo una lista
    return [char for char in texto if char != " "]
# a diferencia del otro ejercicio donde queriamos los caracteres en un str
# aunque tambien podriamos haberlo hecho de esa otra manera y obtener la lista pero seria mas largo


def cuenta_caracteres(listay):  # aqui definimos que le vamos a pasar una lista
    cuenta_diccy = {}
    for char in listay:
        if char in cuenta_diccy:
            # ponemos char porqur le estamos pasando la llave del diccionario
            cuenta_diccy[char] += 1
        else:
            cuenta_diccy[char] = 1
            # quiere decir es que si existe el caracter le vamos a sumar 1 valor
    # y si no se repite le vamos a asginar el valor de 1
    return cuenta_diccy


sin_espacios = no_space_lista(string1)
contados = cuenta_caracteres(sin_espacios)
# con el pprint le tenemos que dar valor de 1 a width
pprint(contados, width=1)


def ordena(dicty):  # a esta funcion le vamos a pasar el diccionario
    return sorted(
        dicty.items(),  # aqui llamamos al metodo de items
        # despues ponemos key que va a indicar el metodo por el cual vamos a ordenar el diccionario
        # y le vamos a indicar que va a recibir la llave: pero que queremos que nos regrese el segundo elemento de la tupla
        key=lambda llave: llave[1],
        reverse=True)  # para que los ordene de manera descendente para que sea mas facil el ejercicio
# ponemos parentesis para pedir que nos devuelva una tupla


ordenados = ordena(contados)
print(ordenados)


def mayores_tuplas(lista):
    # como ya sabemos que el primer elemento de nuestra lista es el mayor
    # podemos usar la sig funcion donde le decimos
    # que queremos acceder al primer elemento
    # y al primer valor de ese elemento para el orden
    maximoy = lista[0][1]
    respuesta = {}
    for ordeny in lista:
        if maximoy > ordeny[1]:
            # aqui definimos que si maximo es mayor que el primer elemento del orden
            # la funcion debe parar
            # pero no lo va a hacer hasta el segundo elemento porque el primero es igual

            break
        # aqui le indicamos el primer valor de la tupla es la llave y el segundo el valor a contar
        respuesta[ordeny[0]] = ordeny[1]
    return respuesta


mayores = mayores_tuplas(ordenados)
print(mayores)


def crea_mensaje(diccionarioy):
    # mensaje con \n para que salte una linea lo sig
    mensajey = "los que más se repiten son: \n"
    # y ahora tenemos que iterar al diccionario para acceder a cada uno de sus elementos
    for keyy, valory in diccionarioy.items():
        mensajey += f"- {keyy} con {valory} repeticiones \n"
    return mensajey


mensaje1 = crea_mensaje(mayores)
print(mensaje1)


def lista_mayus(diccionarioyy):  # indique que le voy a asignar un diccionario
    lista = ""  # le asigne un str para poder usar el metodo uppers despues
    for key in diccionarioyy.items():
        # llame al primer objeto del diccionario que serain las letras
        lista += key[0]

    return lista


# llame a la funcion, aplique upper y lo converti a lista
lista1 = lista_mayus(mayores)
lista1 = lista1.upper()
lista1 = list(lista1)
print(lista1)
