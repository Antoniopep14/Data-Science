saludo = "Hola Global"


def saludar():
    saludo = "Hola Mundo"
    print(saludo)


def saludapepe():
    saludo = "Hola pepe"
    print(saludo)
# las dos variables tienen el mismo nombre
# pero cada una solo tiene alcance dentro de la funcion
# utilizar variables globales en funciones es una mala practica
# y podria dar errores en un futuro


def saludando():
    global saludo  # global va a permitir tomar una variable global
    print(saludo)  # y asignar esa misma variable dentro de la funcion


# pero esto es una pesima practica, por lo que debe evitarse en medida de lo posible
# porque una variable dentro de la funcion podria cambiarte el tipo de dato
# y buscar el error en el codigo de programacion puede ser muy dificil
saludar()
saludapepe()
print(saludo)
saludando()
