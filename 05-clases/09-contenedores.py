# Ahora veremos como meter objetos dentro de otros objetos
# para esto nuestro objetivo va a ser insetar productos dentro de nuestra categoria

class Producto:
    def __init__(self, nombre, precio):
        self.nombre = nombre
        self.precio = precio
# ahora usaremos el metodo str para obtener algo mas bonito al llamar a la instancia

    def __str__(self):
        return f"Producto: {self.nombre} - Precio: {self.precio}"

# ahora tenemos que definir la clase que va a contener nuestros productos


class Categoria:
    productos = []

    # nombre hace referencia al nombre que tendra la categoria
    def __init__(self, nombre, productos):
        # y productos al listado de productos que ella tendra
        self.nombre = nombre
        self.productos = productos

# ahora definiremos un metodo para poder agregar mas productos dentro de la categoria
    def agregar(self, producto):
        # esto lo que va a hacer es agregar un producto al listado de arriba
        self.productos.append(producto)

# ahora def otro metodo para visualizar todo lo que se encuentre guardado en productos
    def imprimir(self):  # para imprimir los productos los vamos a iterar
        for producto in self.productos:
            print(producto)


# ahora creamos productos
kayyak = Producto("Kayak", 1000)
bicicleta = Producto("Bicicleta", 750)
surfboard = Producto("Surfbiard", 500)
# una categoria
# en los parametros le agregamos directamente una lista con los productos que queremos dentro de la categoria
deportes = Categoria("Deportes", [kayyak, bicicleta])
# usamos el metodo de agregar para meter otro producto
deportes.agregar(surfboard)
# y por ultimo usamos el metodo imprimir de la categoria
# y observemos que se conserva el metodo str de Producto
deportes.imprimir()  # Producto: Kayak - Precio: 1000
# Producto: Bicicleta - Precio: 750
# Producto: Surfbiard - Precio: 500
