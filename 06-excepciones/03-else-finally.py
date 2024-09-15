try:
    n1 = int(input("Ingresa primer número: "))
except Exception as ex:
    print("ocurrio un error!")
else:  # se va a ejecutar siempre y cuando no haya ninguna excepcion
    print("No ocurrio ningun error!")  # osea al ingresar un numero int
    # lo que hace else es mantenernos dentro del contexto de try
finally:  # se ejecuta con o sin errores, es decir siempre
    print("se ejecuta siempre!")
