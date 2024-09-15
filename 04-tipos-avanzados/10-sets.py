# set significa grupo o conjunto
# es una conexcion de datos que no se puede repetir y que tampoco esta ordenada
# va con {}
primerSet = {1, 1, 2, 2, 3, 4}
print(primerSet)  # {1, 2, 3, 4}
# solo deja un ocurrencia de cada uno de los datos
# los set se trabajan de manera muy similar a las listas, por lo que podemos usar los mismos metodos
# primerSet.add(5)  # solo puede agregar 1 dato por vez
# primerSet.remove(1) || tambien podemos remover como en listas, etc
# print(primerSet)  # {1, 2, 3, 4, 5}

# tambien podemos crear un set en base a una lista o una tupla
segundo = [3, 4, 5]
segundoSet = set(segundo)
print(segundoSet)  # {3, 4, 5}
# ahora veamos los operadores de set, el primero es |(el que esta a la izq del 1)
set3 = primerSet | segundoSet
print(set3)
print(primerSet | segundoSet)  # {1, 2, 3, 4, 5}
# este se llama operador de union
# esto une los sets que le indiquemos y quita los elementos duplicados
print(primerSet & segundoSet)  # {3, 4}
# esto solo nos da los elementos que se encuentren repetidos entre los set que le indiquemos
# este operador se llama interseccion "&"
print(primerSet - segundoSet)  # {1, 2}
# este es el operador de diferencia y quita los elementos del segundo set al primer set
print(primerSet ^ segundoSet)  # {1, 2, 5}
# este operador se llama diferencia simetrica
# nos va a devolver los elementos que se encuentren en el primero y segundo
# siempre y cuando no esten duplicados entre los 2 sets

# el problema con los set es que no se encuentran ordenados y tampoco podemos acceder a un elemento de estos
# segundoSet[0]   esto daria error
# pero si podemos buscarlo con el iterable if
if 6 in segundoSet:
    print("Si Esta el numero")
else:
    print("no se encuentra el numero")
