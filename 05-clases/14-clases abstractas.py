# Nuestro codigo anterior tiene un grave problema en la clase model
# y es que nosotros podriamos empezar a generar objetos a partir de la clase model
# y esa clase no esta diseñada para generar instancias

from abc import ABC, abstractmethod  # bastrac se usa para propiedades y metodos
# abc es de abstract class y ABC es la clase de la cual debemos heredar
# Esto va a ser para no poder generar instancias de la clase model


class Model(ABC):  # el 1er paso es hacer que herede de ABC

    # def __init__(self):
    #   if not self.tabla:
    #       print("Error, tienes que definir una tabla")
    # 2do paso, despues del constructor tenermos que definir el metodo que vamos a heredar
    # y ya que tenemos la propiedad de la tabla como abstracta ya no necesitamos el constructor
    @property
    @abstractmethod
    def tabla(self):
        pass

# aparte de una propiedad podemos hacer abstracto un metodo
    @abstractmethod
    def guardar(self):
        pass

    @classmethod
    def buscar_por_id(self, _id):
        print(f"buscando por id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"

    def guardar(self):
        print("Guardando usuario")

# model = Model()
# Model.buscar_por_id(123)
# despues de la modificacion da
# TypeError: Can't instantiate abstract class Model with abstract method tabla


usuario = Usuario()
usuario.guardar()  # Guardando usuario
Usuario.buscar_por_id(123)  # buscando por id 123 en la tabla Usuario
