# Ahora veamos como comparar 2 objetos
class Coordenadas:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

# para evitar el error de abajo usamos el metodo mag eq
    def __eq__(self, otro):  # donde otro hace referencia a otra instancia que vamos a comparar
        return self.lat == otro.lat and self.lon == otro.lon

# otro metodo mag que podemos usar para comparar es el de not igual
    def __ne__(self, otro):
        return self.lat != otro.lat or self.lon != otro.lon

# otro metodo seria lt less than
    def __lt__(self, otro):
        return self.lat + self.lon < otro.lat + otro.lon

# otro seria el menor igual
    def __le__(self, otro):
        return self.lat + self.lon <= otro.lat + otro.lon


coords = Coordenadas(45, 27)
coords2 = Coordenadas(45, 27)

print(coords == coords2)  # Arroja false, a pesar de que son iguales
# si cambiamos por , podemos ver que tienen diferente espacio en memoria
print(coords, coords2)  # <__main__.Coordenadas object at 0x000001FFE8F1EB10>
# <__main__.Coordenadas object at 0x000001FFE8F1EB50>
# por eso da False, por que al usar el == nosotros preguntamos si esos 2 objetos son exactamente el mismo

# despues de agregar el metodo magico de eq ahora si da True
print(coords != coords2)  # False, porque son iguales esto es el metodo ne
# aunque si lo quitaramos seguiria dando false, gracias al metodo de eq
print(coords < coords2)
# false, habria que cambiar un valor en coord para ver dif resultado
# ademas, al igual que el metodo eq si preguntaramos > lo contrario
# python asumiria que ese metodo esa valido para ejecutar esa pregunta y no necesitariamos hacer otro para ello
print(coords <= coords2)  # True
