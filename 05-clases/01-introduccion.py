mensaje = "hola Mundo"
# vamos a ver el tipo de dato de la variable mensaje
print(type(mensaje))  # <class 'str'>
# clase: Es el plano de construccion
# objeto: Es una instancia de una clase (lo que construye la clase)

# para crear una clase debemos usar la palabra reservada de class y darle un nombre
# todas las palabras en el nombre de la clase deben de ir la primera con MAYUS
# todas las funciones asociadas a la clase deben de ir identadas y
# dejan de llamarse funcniones para convertirse en metodos
# los metodos son funciones que se encuentran dentro de una clase


class Perro:
    def habla(self):  # siempre se debe de poner self en el parentesis de estos metodos
        print("Guau!")  # como primer parametro


print(Perro)  # <class '__main__.Perro'>
mi_perro = Perro()
print(type(mi_perro))  # <class '__main__.Perro'>
# esto nos devuelve la instancia donde estamos creando nuestro modulo
# ahora vamos a llamar al metodo de habla
mi_perro.habla()  # en los parentesis del metodo que creamos, al momento de llamarlos ya no tenemos que escribir el self
# pero si hubiera algo ademas del self, eso si lo tenemos que agregar

# ahora vamos a verificar si el objeto pertenece o es instancia de algun objeto en particular
# para usar isinstance debemo darle la variable u objeto y despues la instancia sobre la que queremos saber si pertenece
# en este caso Perro
print(isinstance(mi_perro, Perro))  # True

# NOTA: las clases van con MayusEnLaPrimeraPalabra
# las funciones y variable con_guines_bajos
