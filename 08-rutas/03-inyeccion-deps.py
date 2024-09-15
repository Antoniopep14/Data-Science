# import Correa

# class Perro:
#     def __init__(self):
#         self.correa = Correa()
#supongamos que tenemos una clase de perro, que para pasear necesita de una correa definida en self.correa
#para ello importamos Correa, y nuestro constructor se la va a asignar a la clas ede perro
#esto nos genera un problema, por que si por alguna razon queremos reutilizar la clase de perro
#pero en lugar de usar una correa quisiera usar un arnes
#por la forma en que esta construida esta clase, no vamos a poedr hacerlo
#para resolverlo en lugar de importar arriba las clases de las cuales va a depnder mi clase de perro
#lo mejor es que nosotros se la pasemos ya sea con el construtor
#o con un metodo que setee la propiedad
#vamos a ver como seria la primer alternativa

# class Perro:
#     def __init__(self, Correa):
#         self.correa = Correa()

#con esto nosotros conseguimos que independientemente de si le pasamos una correa o un arnes
#siempre y cuando ambas clases tengan los mismos metodos, la clase de perro va a funcionar sin problemas
# de estas manera hacemos reutilizable nuestra clase de perro

#otros 2 ejemplo, un con inyeccion y otro sin inyeccion de dependencias son:

#sin inyeccion
# import usuario

# def guardar():
#     usuario.guardar()

#con inyeccion
# def guardar(entidad):
#     entidad.guardar()

#ese ultimo lo prodriamos usar con productos, twits, fotografias, etc y no solo con usuarios
#ya que solo tendriamos que pasarle la entidad a la clase
#las ventajas de esto son:
#nos permite reutilizar el codigo, nos permite desacoplar el codigo para que sea mas facil de reutilizar
#cuando aprendamos a escribir test nos vamos a dar cuenta que
# va a ser mas facil usarlos con la inyeccion de dependencias

#ahora veamos un ejemplo mas realista:
#algunos frameworks como flask, necesitan que tu aplicacion tengan nu metodo de init_app
#def init_app(bbdd, api):
    #inicializacion de modulo
#de esta manera cuando llamemos a este metodo, dentro de la ejecucion de la aplicacion
#vamos a poder inicializar el modulo
#como configurar rutas de una api, inicializar nuestra base de datos
#y en el caso de que nuestra aplicacion tenga mas paquetes
#tambien vamos a poder importar lo paquetes dentro de nuestra funcion y tambien 
#pasarles una base de datos o cualquier cosa que necesite
#y esto va a hacer que a nuestro modulo sea muy facil escribrirle test



