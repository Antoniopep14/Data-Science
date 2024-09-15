def hola():
    print("Hola Mundo!")
    print("Bienvenido Pepe")


hola()  # de esta manera se llama a las funciones
# De esta manera hola va a imorimir los 2 datos que le metimos a la funcion

# cuando se guarda una funcion deja 2 lineas abajo de la funcion por pep8


def adios(nombre):  # los parentesis se usan para asignar una variable dentro de la funcion
    # estas variables solo se podran usar dentro del contexto de la funcion
    print("Adios Mundo!")
    print(f"Hasta luego {nombre}")


adios("Pepe")  # estas variables son obligatorias
# por lo que debemos asignarle un valor si o si
adios("Axel")  # cuando nosotros llamamos a la funcion lo del () se llama argumento
# dentro de la funcion pasa a llamarse parametro


def tercera(nombre, apellido):  # asi se asignan varios parametros
    print("Hola Mundo!")
    print(f"Hasta luego {nombre} {apellido}")


tercera("Pepe", "Garcia")  # no olvidar las ""
tercera(apellido="garcia", nombre="Pepito")  # esto es un argumenti nombrado
# se usa para dar orden al argumento en caso de no recordar el orden en que debemos ponerlo


# asi le agregamos un argumento por defecto al segundo parametro
def cuarta(nombre, apellido="Feliz"):
    # de esta manera no causa error al ingresar solo el primer argumento
    print("Hola Mundo!")
    print(f"Hasta luego {nombre} {apellido}")


cuarta("Pepe")
