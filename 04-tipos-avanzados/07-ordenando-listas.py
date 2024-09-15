numeros = [2, 4, 1, 45, 75, 22]
# metodo sort ordena nuestra lista
# sort con() los va a ordenar de menor a mayor
# sort(reverse=True) los ordena de mayor a menor

numeros.sort()  # (reverse=True) los ordena alreves
print(numeros)

# funcion sorted
# Esta funcion lo que va a ser es proporcionar una nueva lista
# no va a modificar la lista que ya teniamos anteriormente
# pero igual va a estar ordenada de menor a mayor
# aunque se le puede pasar el valor de ", reverse=True" para ordenarla de mayor a menor
# numeros2 = sorted(numeros) Esto seria normal
numeros2 = sorted(numeros, reverse=True)
print(numeros2)

# al tener un conjunto de listas donde tengamos varios valores dentro
# siempre las va a ordenar dependiendo el primer valor
# en el primer ejemplo de menor a mayor, en el 2do alfabeticamente

usuarios = [[4, "Pepe"], [1, "Axel"], [6, "Jacqueline"]]
usuarios.sort()

print(usuarios)

usuarias = [["Pepe", 4], ["Axel", 1], ["Jacqueline", 6]]
usuarias.sort()
print(usuarias)

# para que ordenara los elementos de la segunda lista
# de menor a mayor debemos de asignarle una funcion
# la sig funcion indica que elemento tomaremos de la lista


def ordena(nombreelem):  # lo que va a hacer esta funcion es dar el elemento
    # por el cual nosotros queremos que el listado sea ordenado
    # donde el indice 0 son nombres y 1 los numeros
    return nombreelem[1]


# ahora usamos el metodo de sort con la funcion ordena
# y usamos "key" para poder darle nombre del parametro
# y despues ya agregamos la funcion
# y si quisieramos que los ordenada al reves, tendriamos que agregarle el metodo ", reverse=True"
# usuarias.sort(key=ordena, reverse=True)
usuarias.sort(key=ordena)
# notesé que no pusimos () despues de la funcion
# porque el metod sort ya esta ejecutando la funcion con los elementos de la lista
print(usuarias)

# FUNCIONES LAMBDA O FUNCIONES ANONIMAS
# vamos a escribir lo de arriba pero de una forma mas eficiente
# usuarias.sort(key=lambda parametros: valorRetorno)
# a lambda tenemos que indicarle 2 valores que son el argumento y los valores
usuarias.sort(key=lambda elemento: elemento[1], reverse=True)
# y esto va a arrojar lo mismo que hicimos arriba con la funcion
print(usuarias)
# poner varias funciones lambda es una mala practica
# pero si solo se va a usar un unica vez en el codigo, adelante!
