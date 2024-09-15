# ahora lo que vamos a hacer es darle una propiedad privada a una clase
# para que una vez que le demos valor, no se pueda modificar
# esto se puede hacer desde el nombre del metodo o dentro del valor del metodo

# aqui vimos la función rename
# para la cual presionamos ctrl + shift + p y escribimos rename
class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre  # para hacerlo privado usamos doble _ entre el . y nombre
        self.edad = edad

    def habla(self):  # nosotros podemos acceder a estas propiedad privadad desde la misma clase sin problema
        # sin embargo no las podemos llamar desde afuera
        print(f"{self.__nombre} dice: Hola!")
# la unica forma en que podriamos acceder a este metodo privado desde afuera
# seria creando otra clase que nos lo arroje

    def get_nombre(self):
        return self.__nombre
# de esta manera obtenemos el nombre de la clase __nombre, pero seguimos sin poder modificarlo
# asi ya estariamos accediendo al valor de la funcion privada
# def __get_nombre(self): tambien podriamos hacer un metodo privado
# para hacer imposible acceder a el desde afuera de la clase
  # para modificar el nombre tendriamos que crear un nuevo metodo
  # #que nos permita hacerlo llamando al metodo

    def set_nombre(self, nombre):
        self.__nombre = nombre

    @classmethod
    def factory(cls):
        return cls("Altair", 9)


persona1 = Persona.factory()
persona1.habla()  # Altair dice: Hola!
print(persona1.get_nombre())  # Altair # y asi obtubimos una propiedad privada
# De esta maenra le cambie el nombre a una clase privada
persona1.set_nombre("Pepe")
persona1.habla()  # Pepe dice: Hola!
# Esto no se deberia de hacer, pero usando __dict__
# podemos acceder a todas las instancias del metodo
print(persona1.__dict__)  # {'_Persona__nombre': 'Pepe', 'edad': 9}
# Esta funcion nos va a dar el nombre de la clase, seguido del nombre de la propiedad
# ahora copiamos la parte a la que queremos acceder
# y de esta manera accedemos a las propiedades privadas de los objetos
print(persona1._Persona__nombre)  # Pepe
# de esta manera estamos accediendo al un valor privado de la clase
# pero es un practica que debe evitarse a toda costa
