from abc import ABC, abstractmethod


class Model(ABC):
    @abstractmethod  # ahora agregamos un metodo abstracto
    def guardar(self):
        pass


class Usuario(Model):
    def guardar(self):
        print("guardando en BBDD")


class Sesion(Model):  # las sesiones son lo que le permiten a un servidor identificar cuando un usuario
    # se esta conectando y a quien pertenece cada peticion que el usuario realiza
    def guardar(self):
        print("guardando en archivo")


# ahora agregamos una funcion de guardar que llame al metodo de guardar
def guardar(entidades):  # que en este caso podrias ser un susuario o una sesion
    for entidad in entidades:
        # si quitamos el for podriamos ejecutar el guardar por separado
        entidad.guardar()


# al tener 2 clases que implementan el mismo metodo significa que nosotros
# podemos ejecuarlos de la misma manera dentro de una funcion
usuario = Usuario()
# guardar(usuario)#guardando en BBDD

sesion = Sesion()
# guardar(sesion)#guardando en archivo
# ahora le entregamos a la funcion de guardar 2 objetos que cumplen con la interfaz necesario para la funcion de guardar
guardar([sesion, usuario])  # guardando en archivo /n guardando en BBDD
