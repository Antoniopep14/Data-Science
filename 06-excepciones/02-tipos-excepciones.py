try:
    n1 = int(input("Ingresa primer número: "))
    adsds  # agregamos esto para ver otro tipo de error al ingresar un int
    # <class 'NameError'>
# Todas las excepciones que ingresen en el codigo de arriba
# van a ser manejadas por el except de abajo
# para saber cual es el tipo de excepcion que arroja vamos a hacer lo sig
# Exception nos da todas las excepciones que puedan salir
except Exception as ex:  # le decimos que ex va a ser igual al otro
    print(type(ex))  # <class 'ValueError'> # para que nos diga el tipo de error
# como ya vimos que el error usual de arriba va a ser ValueError
# podemos definirlo dentro de la excepcion
try:
    n1 = int(input("Ingresa primer número: "))
    asdas  # al hacer lo mismo de arriba el programa se detiene
    # porque no estamos especificando el tipo de error que arroja ahora
    # ", line 15, in <module>
    # asdas NameError: name 'asdas' is not defined
except ValueError as ex:
    print("Ingresa un número válido")
# como tambien sabemos el nombre para la excepcion del error de arriba
# podemos agregar otra excepcion
except NameError as ex:
    print("ocurrio un error")
# asi podemos entregar un mensaje a cada tipo de error
