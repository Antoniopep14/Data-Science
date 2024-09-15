# el constructor es una funcion dentro de una clase que creamos
# que siempre se va a ejecutar cuando creamos una instancia de la clase

class Perro:

    # para hacer un constructor debemos usar __init__ y ponerle self + parametros
    def __init__(self, nombrez):
        # ahora vamos a asignarle un nombre a la clase cuando la estemos instanciando
        self.nombrey = nombrez  # ahora le tenemos que agregar una propiedad a self
        # lo que estamos haciendo es darle valor a nombrez y agregandolo a la propiedad nombrey de la clase
# nombrez y nombrey pueden ser iguales pero los puse dif para notar las referencias
    # una propiedad es una variable que se encuantra asociada a una instancia, que en este caso es una clase

    def habla(self):  # siempre se debe de poner self en el parentesis de estos metodos
        print("Guau!")
# self es una palabra reservada que se encuentra en todas las clases de python y se utilizan para referenciar las instancias de las clases
# self es una referencia a la instancia de la clase
# para el caso de abajo mi_perro vendria siendo self


mi_perro = Perro("Brisa")
# ahora imprimimos y para ello tenemos que llamar a la referencia de la instancia de la clase
# que seria nombrey, no nombrez
print(mi_perro.nombrey)  # Brisa
# de esta manera podemos llamar a la instancia una infinidad de veces
mi_perro2 = Perro("Drako")
print(mi_perro2.nombrey)  # Drako

# ahora vamos a hacer una clase con un constructor extra
# en el siguiente ejemplo ya los ponemos todos igual, arriba era solo referencia


class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad
# Pero ahora abajo hagamos referencia a un constructor de arriba
# para ello tenemos que hacer referecia a self.

    def habla(self):
        print(f"{self.nombre} dice: Hola")


persona1 = Persona("Pepe", "31")
print(persona1.nombre, persona1.edad)  # Pepe 31
persona1.habla()  # Pepe dice: Hola
