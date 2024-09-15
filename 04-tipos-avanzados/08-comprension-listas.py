usuarios = [[4, "Pepe"], [1, "Axel"], [6, "Jacqueline"]]
# ahora de nuestro listado solo queremos obtener el nombre
# Para lo cual vamos a aplicarle una transformacion

# nombres = []
# for usuario in usuarios:
#     nombres.append(usuario[1])
# print(nombres)

# ESTA OPERACION SE CONOCE COMO MAP
# ahora veamos una forma mas elegante de hacer lo mismo de arriba
# nombres = [expresion for item in items]
nombres = [usuario[1] for usuario in usuarios]
print(nombres)

# ESTA OPERACION SE CONOCE COMO FILTER
# y si en lugar de extraer los nombres solo queremos filtrarlos
nombres2 = [usuario for usuario in usuarios if usuario[0] > 2]
# donde if nos va a ayudar a filtar a los usuarios del indice 0 que sean mayores de 2
print(nombres2)

# gracias a estos metodos nosotros podemos crear listas a partir de otras lista ya existente
# ya sea modificando sus elementos, filtrandoslo o ambas cosas

nombres3 = [usuario[1] for usuario in usuarios if usuario[0] > 2]
print(nombres3)
# al ponerle indice a usuario al principio
# estas extrayendo y filtrando con el if
# para crear una tercera lista
# esta operacion usualmente se hace por separado ya que muchos programadores prefieren la programacion funcional

nombres4 = list(map(lambda usuario: usuario[1], usuarios))
print(nombres4)
# list indica que va a ser una nueva lista que va a tener algo de la lista usuarios
# por lo que vamos a trasnformar a los usuarios con map
# y debemos agregarle una funcion a map, en este caso lambda

nombres5 = list(filter(lambda usuario: usuario[0] > 2, usuarios))
print(nombres5)
