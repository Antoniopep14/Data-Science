# En una base de datos nosotros vamos a poder:
# leer, crear, actualizar y eliminar
# leer se refiere a que vamos a poder acceder a su informacion
# ahora vamos a crear una clase que implemente estos metodos, bueno no todos en el mismo
class Model():  # Esta clase de model la vamos a ver mucho en un futuro, se usa mucho esa referecia
    tabla = False  # esto es un atributo de modelo

    def __init__(self):
        if not self.tabla:  # este constructor lo que va a hacer es preguntar si no se encuentra definida esta tabla
            # es decir si nosotros no le hemos asignado ningun valor y en ese caso va a imprimir
            print("Error, tienes que imprimir una tabla")

    def guardar(self):  # aca deberiamos de colocar toda la logica para guardar
        print(f"Guardando {self.tabla} en BBDD")  # BBDD es base de datos

    # colocamos un _ en id porque python tiene un funcion nativa con id
    # pero como un usuario no deberia de buscar por id, vamos a decorarlo con el classmethod
    # sino que eso deberia hacerlo el metodo de clase
    @classmethod  # aunque por la herencia aun permitiria a usuario acceder al metodo
    # pero lo imp es que ya podemos usrlo desde la clase
    def buscar_por_id(self, _id):
        print(f"buscando por id {_id} en la tabla {self.tabla}")


class Usuario(Model):
    tabla = "Usuario"


usuario = Usuario()
usuario.guardar()  # Guardando Usuario en BBDD
Usuario.buscar_por_id(123)  # buscando por id 123 en la tabla Usuario

# y con esto todos los metodos de la clase model podemos usarlo en todas las clases de tablas que queramos
