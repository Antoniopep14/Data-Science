class Persona:
    extremidades = 4  # esto es una verdadera propiedad en la clase
    # es algo que se le va a asignar el mismo dato a todas las instancias al llamar la clase

    def __init__(self, nombre, edad):
        self.nombre = nombre  # para crear propiedad de una instancia estamos usando la palabra
        self.edad = edad  # self.nombre del atributo
    # propiedad es el nombre que se le da en la programacion orientada a objetos, en el compilador es atributo
    # pero conceptualmente propieda y atributo significan lo mismo
    # se hace esta aclaracino poruqe en python hay una clase llamada propiedad, entonces para no confundirnos

    def habla(self):
        print(f"{self.nombre} dice: Hola")


persona1 = Persona("Pepe", "31")  # Pepe 31
print(persona1.nombre, persona1.edad)
print(Persona.extremidades)  # 4 aqui llamamos a la clase
print(persona1.extremidades)  # 4 y aqui a la instancia
# pero tambien podemos cambiar las propiedad de una clase luego de haberla definido
# o solamente camabir el valor para la instancia
# si definimos un valor en la instancia, va a ignorar el de la clase
persona1.extremidades = 5
Persona.extremidades = 2
print(persona1.extremidades)  # 5
print(Persona.extremidades)  # 2
