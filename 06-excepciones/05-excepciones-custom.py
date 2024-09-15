# Tambien podemos lanzar excepciones personalizadas
class MiError(Exception):  # tambien podriamos especificar el tipo de excepcion
    "Esta clase es para representar mi error"
    # tambien podemos ser mas especificos con el error

    def __init__(self, mensaje, codigo):
        self.mensaje = mensaje
        self.codigo = codigo
    # ahora agreguemo un metodo str para definir nuestro error personalizado

    def __str__(self):
        return f"{self.mensaje} - codigo: {self.codigo}"


def division(n=0):
    if n == 0:
        # agregamos un codigo cualquiera para el ejem
        raise MiError("No se puede dividir entre 0", 805)
    return 5/n


try:
    division()
except MiError as e:
    # ahora al imprimir el error podemos acceder al metodo mensaje o codigo *e.codigo, e.mensaje
    print(e)  # No se puede dividir entre 0 - codigo: 805
