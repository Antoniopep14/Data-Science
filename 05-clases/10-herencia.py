# primero un ejemplo para entender lo que es la herrencia
# despues de ver lo de abajo, para solucionar el error de abajo creamos una clase en comun
# que se va a llamar animal
class Animal:
    def comer(self):
        print("comiendo")


class Perro(Animal):  # ahora agremamos () y el nombre de la clase de la cual nosotros queremos heredar sus propiedades y metodos
    def pasear(self):
        print("paseando")

    # def comer(self):
        # print("comiendo")


class Chanchito(Perro):  # ahora le vamos a heredar de perro
    # y entonces tenemos una clase con herencia multinivel, la que haredo de perro y la que perro heredo de animal
    # este tipo de herencia es recomendable no hacerlo mas de 2 niveles
    # def comer(self):
    # print("comiendo")
    def programar(self):
        print("programando")


# el problema con esto es que si tenemos otra clase
# que tambien puede comer entre otras cosas
# cuando queramos cambiar o modificar el metodo de comer
# corremos con el riesgo de olvidar algun metodo dentro de una clase
# y eso podria darnos un error y para ello usamos la herrencia
perro = Perro()  # no olvidar los parentesis
perro.comer()  # comiendo
chanchito = Chanchito()
chanchito.pasear()  # paseando *pudimos usar el pasear porque se lo heredamos de perro
chanchito.comer()  # comiendo
