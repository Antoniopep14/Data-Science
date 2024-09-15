class Animal:
    def comer(self):
        print("comiendo")

    def pasear(self):
        print("paseando animales")


class Perro:
    def pasear(self):
        print("paseando al perro")


class Chanchito(Perro, Animal):  # Podemos darle varias herencias a una clase
    # pero debemos tener cuidado de si esas no tienen una herencia multinivel enlazada
    # porque podrian darnos error en la sintaxis dependiendo el orden en que las ponemos
    # tambien el orden nos dice que herencia tiene priorodad sobre la otra, las de la izq tienen priorodad
    # tambien si no comparten algun metodo, ya que podria arrojarnos el metodo que no queremos

    def programar(self):
        print("programando")


chanchito = Chanchito()
chanchito.pasear()  # paseando al perro
# nos arrojo el pasear del perro porque python toma las herencias de derecha a izquierda
# y las de la izq son las que tienen prioridad por encima de los de la derecha
# Si vamos a heredar multiples clases, tenemos que eliminar o cambiar las clases repetidas
# por esta razon si vamos a heredar, lo mejor es que la clase que va a dar la herencia sean lo mas cortas posibles
# para evitar repetir metodos, aunque tengamos muchas clases heredando
