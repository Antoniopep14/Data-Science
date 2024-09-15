# si quitamos todo el inicio del codigo anterior, esto seguira ejecutandose correctamente
# esot debido a que python tiene tipado dinamico
# no se va a preocupar por verificar si las entidades de la funcino guardar
# provienenen de una extension de clase model a menos ue se lo pidamos
# el problema vendria cuando le pasemos una lista que no tegna definida el metodo de guardar

class Usuario():
    def guardar(self):
        print("guardando en BBDD")


class Sesion():
    def guardar(self):
        print("guardando en archivo")


def guardar(entidades):
    for entidad in entidades:
        entidad.guardar()


usuario = Usuario()

sesion = Sesion()
guardar([sesion, usuario])  # guardando en archivo /n guardando en BBDD
