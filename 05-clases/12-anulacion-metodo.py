# la anulacion de metodo o method override significa que eliminamos o reemplazamos un metodo heredado
class Ave:
    def vuela(self):
        print("vuela ave")


class Pato(Ave):
    def vuela(self):  # al heredar de una clase y definirlo de nuevo, nos quedamos con el metodo de la subclase
        # la palabra reservada de super nos entrega acceso a todos los metodos de la clase padre
        super().vuela()
        print("vuela pato")


pato = Pato()
# pato.vuela()  # vuela pato *esto arroja al no llamar a los metodos de la clase padre
pato.vuela()  # vuela ave /n vuela pato *esto cuando llamamos a los metodos de la clase padre

# pero esto tambien podriamos hacerlo con el constructor


class Perro:
    def __init__(self):
        self.nada = True

    def come(self):
        print("come perro")


class Chihuahua(Perro):
    def __init__(self):
        # dspues de ver lo de abajo llamamos al constructor de la clase padre de la siguiente manera
        super().__init__()
        # lo de abajo ya estaba, solo es lo de arriba
        self.rastrea = True

    def come(self):
        print("come chihuahua")


chihuahua = Chihuahua()
chihuahua.come()
# AttributeError: 'Chihuahua' object has no attribute 'nada'
print(chihuahua.nada, chihuahua.rastrea)
# para evitar este error tenemos que heredarle el constructor de nada desde la clase padre
# tenemos que llamar al construtor por que es donde se esta seteando la propiedad a la instancia
# Despues de eso ya nos arroja True True
# aunque el True podriamos cambiarlo por un string para que nos diga nada, rastrea
