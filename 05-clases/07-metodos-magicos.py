# los metodos magicos son metodos que se van a ejecutar sin que nosotros los llamemos directamente
# todos los metodos magicos inician con __ y terminan con __
class Perro:
    # el contructor de abajo es un metodo magico
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    # Desp de lo de abajo, ahora agregaremos el metodo mag destructor
    # esto lo que hara será quitar la instancia de la clase
    def __del__(self):
        print(f"chao perro {self.nombre}")

# ahora veamos el metodo magico str, para lo cual lo vamosa definir en un metodo
# de esta manera le estamos agregando ese str a la variable str perro de la instancia
    def __str__(self):
        return f"Clase Perro: {self.nombre}"

    def habla(self):
        print(f"{self.nombre} dice: Guau!")


# al hacer esto el constructor se ejecuta automaticamente y de manera indirecta
perro = Perro("Brisa", 4)
# agregando los valores de nmobre y edad a la clase
# si queremos ver todos los metodo magicos solo hay que escribir la instancia.
# perro.  y automaticamente apareceran todos los metodos magicos
# o visitar https://rszalski.github.io/magicmethods/
# Esto es gracias a la herencia que la clase Perro le entrega
print(Perro)  # <class '__main__.Perro'>
print(perro)  # Clase Perro: Brisa
print(perro.nombre, perro.edad)  # Brisa 4
# Transformamos la instancia, pero desde el metodo magico de str de la clase
texto = str(perro)
print(texto)  # Clase Perro: Brisa
del perro  # chao perro Brisa *puede ser con () o sin ellos
# print(perro) NameError: name 'perro' is not defined. Did you mean: 'Perro'?
