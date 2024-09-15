#veamos como generar numeros aleatorios entre otras cosas
import random
print(random.random())#0.39681795232944683
#nos va a dar un numero entre 0 y 1
#si queremos un numero entre 0 y 100 solo lo multiplicamos por 100 y asi sucesivamente
print(random.randint(1, 10))
#esto nos permite generar un numero entre 2 parametros que le asignemos

#ahora desordenemos una lista
lista = [1, 2, 3, 4, 5, 6, 7, 8]
random.shuffle(lista)
print(lista)#y lo revuelve de dif manera cada que ejecutamos

#ahora ecogeremos un numero aleatorio de la lista
lista2 = [1, 2, 3, 4, 5, 6, 7, 8]
print(random.choice(lista2))
#pero si queremos 3 o 4 o la mitad de valores ahora usamos
print(random.choices(lista2, k=3))#aqui le damos la cantidad de elementos que queremos k=
#tambien funciona con str
print(random.choices("abcdefghi.,123", k=4))
#con esto podemos generar contraseñas aleatorias
#cadenas de caracteres aleatorios, identificadores unicos
print("".join(random.choices("abcdefghi.,123", k=4)))#nos da algo aleatorio de esto

##ahora crearemos una contraseña, afortunadamente existe un modulo en python que contiene todos los caracteres validos
import string
chars = string.ascii_letters
digitos = string.digits
seleccion = random.choices (chars + digitos, k=16)
contrasena = "".join(seleccion)
print(contrasena)



