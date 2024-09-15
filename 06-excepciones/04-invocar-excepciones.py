# ahora veamos como invocar excepciones dentro del codidgo
def division(n=0):
    if n == 0:
        # buscamos la excepcion en google, escribimos python errors and exceptions
        # debemos evitar las excepciones generales o Exception, porque nos dice que son muy globales
        raise ZeroDivisionError("No se puede dividir entre 0")
    return 5/n  # no se puede dividir entre 0 entonces agregamos un metodo if


try:
    division()
except ZeroDivisionError as e:  # ahora llamamos a la excepcion
    # esto es aplicable a todas las excepciones
    print(e)
# es recomendable no lanzar excepciones seguido porque consumen mucho procesador
