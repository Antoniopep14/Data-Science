class Persona:
    extremidades = 4

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod  # Esto lo que va a hacer es tomar el metodo de habla
    # y lo va a traansformar en un metodo directo de la clase de persona
    def habla(cls):  # cls es una convencion que hace referencia a la clase misma
        # que seria lo mismo que si escribieramos Persona
        print("Hola")

    @classmethod
    def persona3(cls):  # esto es conocido como factory
        return cls("Altair", 9)


Persona.habla()  # Hola
persona1 = Persona("Pepe", 31)
persona2 = Persona("Anel", 29)
persona3 = Persona.persona3()
# Para hacer esto podriamos crear un metodo que nos cree una instancica
# Esto se le conoce como factory method
print(persona3.nombre, persona3.edad)  # Altair 9
