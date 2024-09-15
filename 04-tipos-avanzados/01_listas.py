numeros = [1, 2, 3]  # aparte de asignar el indice de un string
# el [] nos indica el inicio y fin de una lista
# cada elemento debe ir separado por una , hasta el ultimo, ese ya no lleva ,

letras = ["a", "b", "c"]  # podemos colocar str dentro de la lista
# y pueden tener los elementos que queramos
booleans = [True, False]  # Lista de booleans
matriz = [[0, 1], [1, 0]]  # cada corchete va separado por ,
# esto es un listado dentro de un listado
ceros = [0] * 10  # Es lo mismo que ceros = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
alfanumerico = numeros + letras  # estamos juntando 2 listas
# esto da [1, 2, 3, 'a', 'b', 'c']
rango = list(range(10))  # usamos la funcion list y range para crear una lista
# que contiene los numeros del 0 al 10
# da [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# recordar que se queda 1 valor antes del que especificamos
rango2 = list(range(1, 11))
# da [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# da ['h', 'o', 'l', 'a', ' ', 'm', 'u', 'n', 'd', 'o']
chars = list("hola mundo")
print(chars)
