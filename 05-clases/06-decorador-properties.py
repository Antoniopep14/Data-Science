# ahora tenemos que implementar logica al constructor para que el nombre de la clase
# no sea un espacio en blanco, un boolean o cualquier cosa que no deseamos

class Perro:
    def __init__(self, nombre):
        # modificamos el constructor para agregar la funcion de abajo
        self.set_nombre(nombre)

# tenemos que crear otro metodo para poder acceder a la propiedad en la misma instamcia
    def set_nombre(self, nombre):
        if nombre.strip():  # si el nombre es strip lo seteamos, sino regresamos nada
            self.__nombre = nombre
        return
# como hicimos privada la propiedad de arriba, necesitamos agregar un get al return
# para que nos devuelva el valor del metodo, ya que no podemos acceder a el desde afuera

    def get_nombre(self):
        return self.__nombre


perro = Perro("Brisa")
# ahora hagamoslo sin llamas al modulo de la clase
print(perro)  # <__main__.Perro object at 0x000001DD271CE310>
# los numeros al final son el espacio en memoria
print(perro.get_nombre())  # Brisa #no olvidar los parentesis despues del metodo
# el problema con esto es que el autocompletado nos motraria despues del metodo
# perro.get_nombre, perro.set_nombre, perro.__nombre
# y no sabriamos cual usar


class Persona:
    def __init__(self, nombre):
        self.nombre = nombre  # despues de hacer lo de abajo
        # modificamos el constructor self.nombre(nombre)
        # para decirle que self.nombre va a ser igual al nombre que le pasemos
        # y automaticamente todo va a pasar por el verificador de setter
# para resolver el problema de arriba usamos el decorador @property
# y dentro de el incluimos el get nombre

    @property
    def nombre(self):  # le quitamos el get para enlazarlo a los decoradores
        return self.__nombre
# el decorador de property va a crear otro decorador con el nombre que le hayamos dado
# al primer decorador de arriba

    @nombre.setter  # y usamos el metodo setter para indicarle cual va a ser la propiedad de nombre
    def nombre(self, nombre):  # Entonces quitamos el set_, para que quede enlazado al nombre del decorador
        # y al de arriba
        # esto solo se puso para veificar que esta pasando por aqui antes de entregar el nombre
        print("pasando por setter")
        if nombre.strip():  # si es un strip darle nombre, sino regresamos nada
            self.__nombre = nombre
        return


persona1 = Persona("Pepe")
print(persona1.nombre)  # pasando por setter /n Pepe
